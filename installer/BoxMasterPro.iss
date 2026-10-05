# -*- mode: python ; coding: utf-8 -*-

from pathlib import Path

ROOT = Path(__file__).resolve().parent

# Gerekli dosyalar / assets
try:
    root_assets = ROOT / "assets"
    root_assets.mkdir(exist_ok=True)
except Exception:
    pass

# Dosya bilgileri
AppName = "BoxMaster Pro"
AppVersion = "1.2.0"
OutputFileName = "BoxMasterPro-Setup"

[Setup]
AppName={#AppName}
AppVersion={#AppVersion}
DefaultDirName={autopf}\BoxMasterPro
DefaultGroupName={#AppName}
OutputDir={#ROOT}\installer\Output
OutputBaseFilename={#OutputFileName}
Compression=lzma
SolidCompression=yes
WizardSmallImageFile={#ROOT}\assets\boxmaster_splash.png
SetupIconFile={#ROOT}\assets\boxmaster_icon.ico
AppId={{F8F6C5B2-0F74-4D5E-B2F2-2E2E24F2D8C1}}
PrivilegesRequired=lowest

[Languages]
Name: "turkish"; MessagesFile: "compiler:Languages\Turkish.isl"

[Files]
Source: "{#ROOT}\dist\BoxMasterPro.exe"; DestDir: "{app}"

[Icons]
Name: "{group}\BoxMaster Pro"; Filename: "{app}\BoxMasterPro.exe"
Name: "{commondesktop}\BoxMaster Pro"; Filename: "{app}\BoxMasterPro.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\BoxMasterPro.exe"; Description: "BoxMaster Pro'ü başlat"; Flags: nowait postinstall skipifsilent

