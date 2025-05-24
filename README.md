# 逆水寒手游PC自动弹琴

这是一个支持在Windows端自动读取`midi`文件并演奏的逆水寒手游PC弹琴脚本，基于(https://github.com/WitchElaina/Genshin_Zither_Player) 二次开发

## 使用方法

注意！运行软件需要先打开游戏，并且以管理员身份运行NishuihanMPlayer！

使用时请将BPM控制在合理范围内！

1.从release下载包体，解压运行 NishuihanMPlayer.exe

2.选择midi文件，设定BPM，点击play后自动激活游戏窗口并演奏

### MIDI文件格式

支持标准midi文件，请注意，midi文件仅支持钢琴白键！

演奏仅支持CMajor，否则会自动升/降调。

### 导入自定义MIDI

将midi文件放在`midi_repo`文件夹内, 打开程序即可正常加载演奏

### 编译

1.pyinstaller编译GUI.spec

2.解压midi_repo并放在程序根目录

### 改进

使用了win32模拟键盘输入，从而绕过游戏的检测机制

添加了点击开始后自动聚焦到目标窗口的功能

解决了高速演奏音符时产生的歌曲降速问题