# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(545, 375)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(314, 250))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.widget_4)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox_bpm = QtWidgets.QSpinBox(self.widget)
        self.spinBox_bpm.setEnabled(False)
        self.spinBox_bpm.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBox_bpm.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox_bpm.setAccelerated(True)
        self.spinBox_bpm.setMinimum(40)
        self.spinBox_bpm.setMaximum(2000)
        self.spinBox_bpm.setProperty("value", 120)
        self.spinBox_bpm.setObjectName("spinBox_bpm")
        self.gridLayout.addWidget(self.spinBox_bpm, 2, 1, 1, 1)
        self.comboBox_mid_name = QtWidgets.QComboBox(self.widget)
        self.comboBox_mid_name.setObjectName("comboBox_mid_name")
        self.comboBox_mid_name.addItem("")
        self.gridLayout.addWidget(self.comboBox_mid_name, 0, 1, 2, 1)
        self.comboBox_key = QtWidgets.QComboBox(self.widget)
        self.comboBox_key.setEnabled(False)
        self.comboBox_key.setObjectName("comboBox_key")
        self.gridLayout.addWidget(self.comboBox_key, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 2, 1)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.widget_4)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_play = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_play.setObjectName("pushButton_play")
        self.horizontalLayout.addWidget(self.pushButton_play)
        self.pushButton_end = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_end.setEnabled(True)
        self.pushButton_end.setObjectName("pushButton_end")
        self.horizontalLayout.addWidget(self.pushButton_end)
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.spinBox_sec = QtWidgets.QSpinBox(self.widget_2)
        self.spinBox_sec.setMinimum(2)
        self.spinBox_sec.setMaximum(20)
        self.spinBox_sec.setObjectName("spinBox_sec")
        self.horizontalLayout.addWidget(self.spinBox_sec)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_5 = QtWidgets.QWidget(self.widget_4)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_show = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_show.setObjectName("pushButton_show")
        self.horizontalLayout_4.addWidget(self.pushButton_show)
        self.checkBox_popup = QtWidgets.QCheckBox(self.widget_5)
        self.checkBox_popup.setEnabled(False)
        self.checkBox_popup.setObjectName("checkBox_popup")
        self.horizontalLayout_4.addWidget(self.checkBox_popup)
        self.verticalLayout.addWidget(self.widget_5)
        self.widget_3 = QtWidgets.QWidget(self.widget_4)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_info = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_info.setFont(font)
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setWordWrap(True)
        self.label_info.setObjectName("label_info")
        self.horizontalLayout_2.addWidget(self.label_info)
        self.verticalLayout.addWidget(self.widget_3)
        self.horizontalLayout_3.addWidget(self.widget_4)
        self.widget_6 = QtWidgets.QWidget(self.centralwidget)
        self.widget_6.setEnabled(True)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(self.widget_6)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)
        self.widget_7 = QtWidgets.QWidget(self.widget_6)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_clear = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout_5.addWidget(self.pushButton_clear)
        self.pushButton_export = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_export.setObjectName("pushButton_export")
        self.horizontalLayout_5.addWidget(self.pushButton_export)
        self.verticalLayout_2.addWidget(self.widget_7)
        self.horizontalLayout_3.addWidget(self.widget_6)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NishuihanM Auto Player"))
        self.comboBox_mid_name.setItemText(0, _translate("MainWindow", "Please Select.."))
        self.label.setText(_translate("MainWindow", "Midi Name / 曲名"))
        self.label_3.setText(_translate("MainWindow", "Key / 移调"))
        self.label_2.setText(_translate("MainWindow", "BPM / 曲速"))
        self.pushButton_play.setText(_translate("MainWindow", "Start"))
        self.pushButton_end.setText(_translate("MainWindow", "Exit"))
        self.label_4.setText(_translate("MainWindow", "等待时间"))
        self.pushButton_show.setText(_translate("MainWindow", "显示文字谱"))
        self.checkBox_popup.setText(_translate("MainWindow", "窗口置顶"))
        self.label_info.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_clear.setText(_translate("MainWindow", "清除"))
        self.pushButton_export.setText(_translate("MainWindow", "导出"))
