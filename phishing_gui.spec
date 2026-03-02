# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['phishing_gui.py'],
    pathex=[],
    binaries=[],
    datas=[('Data\\spamassassin\\phishing_model.pkl', 'Data\\spamassassin'), ('Data\\spamassassin\\vectorizer.pkl', 'Data\\spamassassin')],
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
    name='phishing_gui',
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
