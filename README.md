# BoxMasterPro - Production Release

## Overview

BoxMasterPro v1.2.0 - Professional boxing training assistant with modern dark mode UI and complete production-ready packaging.

## Features

✨ **Core Features**
- Modern dark theme UI (dark mode)
- Random punch combination generator (7+ punch types)
- Intelligent round and rest timer management
- Audio alerts for work/rest transitions
- Professional user interface with card-based layout
- Version 1.2.0 with semantic versioning

📦 **Production Features**
- Custom application icon (256x256 PNG/ICO)
- Professional splash screen on startup
- Windows installer (Inno Setup) - fully customizable
- Portable ZIP distribution (no installation required)
- Release notes and changelog management
- Build manifest for version tracking
- Complete version management system
- Update checking system for GitHub releases

🛠️ **Developer Tools**
- Unified CLI build tool (`build_cli.py`)
- Automated asset generation
- Version bumping (major/minor/patch)
- Release manager with history tracking
- Production build pipeline
- Build artifact cleanup

## Installation

### Option 1: Use Installer (Recommended)
1. Download `BoxMasterPro-Setup.exe`
2. Double-click to run installer
3. Follow setup wizard
4. Launch from Start Menu or Desktop

### Option 2: Portable Version
1. Download and extract `BoxMasterPro-{VERSION}-portable.zip`
2. Run `BoxMasterPro.exe` directly
3. No installation needed

### Option 3: From Source
```bash
git clone https://github.com/metinhasimi22/BoxMasterPro.git
cd BoxMasterPro
pip install -r requirements.txt
python main.py
```

## Building from Source

### Quick Build
```bash
python build_cli.py build --full
```

### Step-by-Step
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Generate assets
python generate_assets.py

# 3. Build EXE
python build_exe.py

# 4. Create installer (requires Inno Setup)
python build_cli.py build --full
```

## Directory Structure

```
BoxMasterPro/
├── main.py                    # Main application
├── version.py                 # Version management
├── app_utils.py              # Application utilities
├── build_cli.py              # Unified build CLI
├── build_production.py        # Full production builder
├── build_exe.py              # PyInstaller wrapper
├── generate_assets.py         # Icon/splash generator
├── version_manager.py         # Version manager
├── release_manager.py         # Release/update manager
├── requirements.txt           # Python dependencies
├── VERSION                    # Current version file
├── version_info.txt          # Windows version info
├── BUILD_GUIDE.md            # Complete build guide
├── README.md                 # This file
├── assets/                    # Application resources
│   ├── boxmaster_icon.ico
│   ├── boxmaster_icon.png
│   └── boxmaster_splash.png
├── installer/                 # Inno Setup files
│   ├── BoxMasterPro.iss      # Installer script
│   └── Output/               # Built installers
└── releases/                  # Release history
    ├── releases.json
    └── CHANGELOG_*.md
```

## Version Management

### Current Version: 1.2.0

### Bumping Version
```bash
python build_cli.py version bump --part patch   # 1.2.0 → 1.2.1
python build_cli.py version bump --part minor   # 1.2.0 → 1.3.0
python build_cli.py version bump --part major   # 1.2.0 → 2.0.0
```

### Custom Version
```bash
python build_cli.py version write --version 2.0.0
```

## Release Management

### Create Release
```bash
python build_cli.py release add --version 1.2.0 --changelog "Major new features and improvements"
```

### List Releases
```bash
python build_cli.py release list
```

### Check for Updates
```bash
python build_cli.py release check
```

## System Requirements

- **Windows**: 7 or later
- **Memory**: 50+ MB free disk space
- **Display**: 1024x600 minimum resolution recommended
- **No internet required** (optional for update checking)

## Application Structure

### Main Components
1. **BoxMasterApp** - Main application class with UI
2. **SplashScreen** - Professional startup screen
3. **Audio System** - Cross-platform sound alerts
4. **Version Management** - Semantic versioning
5. **Release Manager** - Release history and updates

### Audio Alerts
- Work phase start: 880 Hz beep
- Rest phase: 660 Hz beep
- Workout complete: 3-tone melody

## Supported Platforms

| Platform | Build | Run | Installer |
|----------|-------|-----|----------|
| Windows 10/11 | ✓ | ✓ | ✓ |
| Windows 7/8 | - | ✓ | ✓ |
| macOS | ✓ | ✓ | - |
| Linux | ✓ | ✓ | - |

## Configuration

Application settings can be customized in `version.py`:
```python
APP_NAME = "BoxMasterPro"
VERSION = "1.2.0"
```

UI colors can be modified in `main.py` theme constants.

## Troubleshooting

### Application won't start
- Verify Windows 7+ installation
- Check disk space (50+ MB free)
- Try portable version

### No audio alerts
- Check Windows volume settings
- Verify speaker connectivity
- Application uses Windows native `winsound` API

### Build issues
- Ensure Python 3.7+ installed
- Run `pip install -r requirements.txt` to update deps
- Check internet connection for Inno Setup download

## FAQ

**Q: Is internet required?**
A: No, application works offline. Update checking is optional.

**Q: Can I customize the timer duration?**
A: Yes, modify `work_duration` and `rest_duration` in `main.py` (lines ~38-40).

**Q: How do I modify punch combinations?**
A: Edit the `punches` list in `main.py` (lines ~32-39).

**Q: Can I run multiple instances?**
A: Yes, each instance runs independently.

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit changes with clear messages
4. Submit a pull request

## License

MIT License - See LICENSE file for details

## Support

- **Issues**: https://github.com/metinhasimi22/BoxMasterPro/issues
- **Discussions**: https://github.com/metinhasimi22/BoxMasterPro/discussions
- **Email**: metinhasimi22@github.com

## Changelog

### v1.2.0 (2026-10-05)
- ✨ Full production-ready package
- 🎨 Custom application icon and splash screen
- 📦 Windows installer support
- 🔊 Cross-platform audio alerts
- 📝 Version and release management
- 🛠️ Unified CLI build tool
- 📊 Build manifest and release notes

### v1.0.0
- Initial release
- Core training features
- Dark mode UI

## Credits

Developed with ❤️ for boxing enthusiasts.

---

**BoxMasterPro** - Your Professional Boxing Training Assistant
