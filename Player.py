import mido
import os
import time
import ctypes
from ctypes import wintypes

# Key Map between midi file and Keyboard
KEY_MAP = {60:'z',62:'x',64:'c',65:'v',67:'b',69:'n',71:'m',72:'a',74:'s',76:'d',77:'f',79:'g',81:'h',83:'j',84:'q',86:'w',88:'e',89:'r',91:'t',93:'y',95:'u',0:'p'}

SCALES = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

# Scan midi file in mid_repo folder
def midScanner():
    m_file = os.listdir("."+os.sep+"midi_repo")
    ret = []
    for i in m_file:
        if os.path.splitext(i)[1] == '.mid':
            ret.append(i)
    return ret
            


# Translate midi note to keybord
def noteTrans(m_note_value):
    return KEY_MAP[m_note_value]

# Player only support melody in C Major, Use this to translate other scale to C Major
def allToCMajor(m_file_name):
    file_name = "." + os.sep + "midi_repo" + os.sep + m_file_name
    # print(file_name)
    note_temp = []
    avialiable_add = []
    for msg in mido.MidiFile(file_name):
        # if(msg.type == "note_on" or msg.type == "note_off"):
        if(msg.type == "note_on"):
            isExist = False
            for i in note_temp:
                if(i==msg.note):
                    isExist = True
                    break;
            if(not isExist): 
                note_temp.append(msg.note)
    

    for i in range(-48,48):
        isC = True
        for cur in note_temp:
            if(KEY_MAP.__contains__(int(cur)+i)==False):
                isC = False
                break
        if(isC):
            avialiable_add.append(i)
    return avialiable_add
            
        
        

# 添加 SendInput 相关定义
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

def playMidi(m_file_name, m_bpm, m_key_add):
    file_name = "." + os.sep + "midi_repo" + os.sep + m_file_name
    real_time = float( 120 / m_bpm ) 
    midi = mido.MidiFile(file_name)
    
    # SendInput 函数指针
    SendInput = ctypes.windll.user32.SendInput
    MapVirtualKey = ctypes.windll.user32.MapVirtualKeyW
    
    def send_key(key, is_press):
        vk_code = ord(key.upper())
        scan_code = MapVirtualKey(vk_code, 0)
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        
        # 根据是按下还是释放设置不同的标志
        flags = 0 if is_press else 0x0002
        ii_.ki = KeyBdInput(vk_code, scan_code, flags, 0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(1), ii_)
        SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    # 记录当前按下的键
    pressed_keys = set()
    
    # Read midi file
    for msg in midi:
        if msg.time > 0:
            time.sleep(float(msg.time) * real_time)
            
        if msg.type == "note_on" and msg.velocity > 0:
            key = noteTrans(int(msg.note) + m_key_add)
            send_key(key, True)  # 按下按键
            pressed_keys.add(key)
        elif (msg.type == "note_off") or (msg.type == "note_on" and msg.velocity == 0):
            if msg.type == "note_on":
                note = int(msg.note) + m_key_add
            else:
                note = int(msg.note) + m_key_add
            key = noteTrans(note)
            if key in pressed_keys:
                send_key(key, False)  # 释放按键
                pressed_keys.remove(key)

def counter(m_second):
    for i in range(m_second):
        time.sleep(1)