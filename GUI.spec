# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['GUI.py', 'SheetMaker.py', 'Player.py', 'mainwindow_ui.py'],
    pathex=[r'C:\Users\admin\Desktop\Genshin_Zither_Player-master'],
    binaries=[],
    datas=[
        ('midi_repo', 'midi_repo'),
        ('icon.ico', '.'),  # 确保图标文件会被复制到程序目录
    ],
    hiddenimports=['win32gui', 'win32con'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='NishuihanMPlayer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico'  # 添加这一行
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='NishuihanMPlayer',
)
