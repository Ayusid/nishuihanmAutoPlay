import sys,os
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtCore
import Player as GZP
from mainwindow_ui import Ui_MainWindow
import ctypes
import SheetMaker as GSM
import win32gui
import win32con


def is_admin():
    try:
        if(os.sep=='/'):
            return True
        else:
            return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
class Thread(QtCore.QThread):
    wait_time = 0
    file_name = ""
    keyadd = 0
    bpm = 0
    
    def __init__(self, m_wait_time, m_file_name, m_keyadd, m_bpm):
        super(Thread,self).__init__()
        self.wait_time = m_wait_time
        self.file_name = m_file_name
        self.keyadd = m_keyadd
        self.bpm = m_bpm
        
    def run(self):
        # 获取并激活游戏窗口
        hwnd = win32gui.FindWindow(None, "逆水寒手游桌面版")
        if hwnd:
            win32gui.SetForegroundWindow(hwnd)
            win32gui.SetActiveWindow(hwnd)
        
        GZP.counter(self.wait_time)
        GZP.playMidi(self.file_name, self.bpm, self.keyadd)
        
        
    def stop(self):
        self.terminate()

        
        
class GUI(QMainWindow, Ui_MainWindow):
    count_sec = 5
    
    key_adds = []
    playThread = Thread
    def __init__(self, parent=None):
        super(GUI, self).__init__(parent)
        self.setupUi(self)
        
        # 设置窗口图标
        from PyQt5.QtGui import QIcon
        import os
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icon.ico')
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
            # 设置所有子窗口和按钮的图标
            app = QApplication.instance()
            app.setWindowIcon(QIcon(icon_path))
        
        # 原有的初始化代码
        self.comboBox_mid_name.addItems(GZP.midScanner())
        self.comboBox_mid_name.currentIndexChanged.connect(self.midiSelected)
        
        self.pushButton_end.setEnabled(False)
        self.pushButton_end.setAutoRepeat(False)
        self.pushButton_export.setEnabled(False)
        self.pushButton_end.pressed.connect(self.stop)
        self.pushButton_end.clicked.connect(self.showEndPlayinfo)
        
        self.pushButton_play.clicked.connect(self.playMidi)
        self.pushButton_play.pressed.connect(self.showPlayinfo)
        
        self.spinBox_sec.setValue(5)
        self.label_info.setText('NishuihanMPlayer@NANAM1,2025')
        
        self.pushButton_show.clicked.connect(self.sheetGen)
        self.checkBox_popup.clicked.connect(self.poupWindow)
        
        self.pushButton_clear.clicked.connect(self.textEdit.clear)
        self.pushButton_export.clicked.connect(self.sheetExport)

        
    def midiSelected(self):
        if(self.comboBox_mid_name.currentIndex()!=0):
            # Enable bpm and key selector
            self.comboBox_key.setEnabled(True)
            self.spinBox_bpm.setEnabled(True)
            
            # Scan avialable keys
            avlb_key = []
            self.comboBox_key.clear()
            avlb_key.clear()
            self.key_adds.clear()
            
            if(not( GZP.allToCMajor(self.comboBox_mid_name.currentText()))):
                self.label_info.setText('Midi out of range! Please select another.')
                self.comboBox_key.setEnabled(False)
                self.pushButton_play.setEnabled(False)
                self.pushButton_export.setEnabled(False)
                
            else:
                for i in GZP.allToCMajor(self.comboBox_mid_name.currentText()):
                    if(i>0):
                        avlb_key.append("+"+str(i)+"key")
                        self.key_adds.append(i)
                    elif(i<=0):
                        avlb_key.append(str(i)+"key")
                        self.key_adds.append(i)
                self.comboBox_key.addItems(avlb_key)
                self.label_info.setText('当前选中: '+self.comboBox_mid_name.currentText())
                self.comboBox_key.setEnabled(True)
                self.pushButton_play.setEnabled(True)
                self.pushButton_export.setEnabled(True)
            
        else:
            self.comboBox_key.setEnabled(False)
            self.spinBox_bpm.setEnabled(False)
            self.pushButton_export.setEnabled(False)
            self.label_info.setText('NishuihanMPlayer@NANAM1,2025')
            
    def playMidi(self):
        # Player init
        wait_time = int(self.spinBox_sec.value())
        file_name = self.comboBox_mid_name.currentText()
        bpm = int(self.spinBox_bpm.value())
        key_add = int(self.key_adds[self.comboBox_key.currentIndex()])
        self.playThread = Thread(wait_time, file_name, key_add, bpm)
        self.playThread.start()
            
    def stop(self):
        self.playThread.stop()

        
    def showPlayinfo(self):
        self.label_info.setText('请点击窗口内任意处')
        self.comboBox_key.setEnabled(False)
        self.comboBox_mid_name.setEnabled(False)
        self.pushButton_end.setEnabled(True)
        self.spinBox_bpm.setEnabled(False)
        self.spinBox_sec.setEnabled(False)
        self.pushButton_export.setEnabled(False)
        self.pushButton_play.setText('Playing..')
        
    def showEndPlayinfo(self):
        self.label_info.setText('NishuihanMPlayer@NANAM1,2025')
        self.pushButton_end.setEnabled(False)
        self.comboBox_key.setEnabled(True)
        self.comboBox_mid_name.setEnabled(True)
        self.spinBox_bpm.setEnabled(True)
        self.spinBox_sec.setEnabled(True)
        self.pushButton_export.setEnabled(True)
        self.pushButton_play.setText('Play')
        
    def poupWindow(self):
        self.setWindowFlags(self.windowFlags | QtCore.Qt.WindowStaysOnTopHint)

        
    def sheetGen(self):
        # init
        file_name = self.comboBox_mid_name.currentText()
        bpm = int(self.spinBox_bpm.value())
        key_add = int(self.key_adds[self.comboBox_key.currentIndex()])
        
        sheet = GSM.printMidiSheet(file_name, key_add)
        for notes in sheet:
            self.textEdit.append(str(notes))
            
    def sheetExport(self):
        self.textEdit.selectAll()
        self.textEdit.copy()
        self.label_info.setText("已导出至剪贴板!")

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        if is_admin():
            window = GUI()
            window.show()
            sys.exit(app.exec_())
        else:
            if sys.version_info[0] == 3:
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
            else:
                ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
    except Exception as e:
        print(f"Error: {str(e)}")
        input("按回车键退出...")  # 添加这行以便查看错误信息
        
        