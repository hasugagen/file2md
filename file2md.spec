# -*- mode: python ; coding: utf-8 -*-
import os
import magika

# magikaライブラリのパスを取得
magika_path = os.path.dirname(magika.__file__)

a = Analysis(
    ['src\\main.py'],
    pathex=[],
    binaries=[],
    datas=[
        (os.path.join(magika_path, 'models'), 'magika/models'),
        (os.path.join(magika_path, 'config'), 'magika/config'),
    ],
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
    name='file2md',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
