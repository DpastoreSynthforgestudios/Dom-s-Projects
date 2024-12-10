# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['SDM.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\coold\\p\\bg.png', '.'), ('C:\\Users\\coold\\p\\ship.png', '.'), ('C:\\Users\\coold\\p\\star.png', '.'), ('C:\\Users\\coold\\p\\mm bg.png', '.'), ('C:\\Users\\coold\\p\\bg still.jpeg', '.'), ('C:\\Users\\coold\\p\\gta.mp3', '.'), ('C:\\Users\\coold\\p\\Resilience.ogg', '.'), ('C:\\Users\\coold\\p\\music.ogg', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='SDM',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
