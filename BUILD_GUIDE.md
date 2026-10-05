# BoxMasterPro Production Build Guide

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. One-Command Full Build
```bash
python build_cli.py build --full
```

This will:
- Generate assets (icon, splash screen)
- Build Windows EXE
- Create installer (requires Inno Setup)
- Create portable ZIP
- Generate release notes
- Create build manifest

## Detailed Commands

### Building
```bash
# Build EXE only
python build_cli.py build

# Full production build
python build_cli.py build --full

# Build without regenerating assets
python build_cli.py build --no-assets
```

### Version Management
```bash
# Read current version
python build_cli.py version read

# Bump version (patch, minor, major)
python build_cli.py version bump --part patch
python build_cli.py version bump --part minor
python build_cli.py version bump --part major

# Set specific version
python build_cli.py version write --version 2.0.0

# Get version info
python build_cli.py version info
```

### Release Management
```bash
# Add a release
python build_cli.py release add --version 1.2.0 --changelog "Fixed bugs, added features"

# List all releases
python build_cli.py release list

# Check for updates
python build_cli.py release check

# Show changelog for version
python build_cli.py release changelog --version 1.2.0
```

### Cleanup
```bash
# Clean build artifacts
python build_cli.py clean

# Remove all build files
python build_cli.py clean --all
```

## Output Structure

After a full build:
```
installer/Output/
├── BoxMasterPro.exe              # Standalone executable
├── BoxMasterPro-Setup.exe        # Windows installer
├── BoxMasterPro-1.2.0-portable.zip  # Portable version
├── RELEASE_NOTES_v1.2.0.txt      # Release notes
├── build_manifest.json           # Build metadata
└── releases/
    ├── releases.json             # Release history
    └── CHANGELOG_v1.2.0.md       # Version changelog
```

## System Requirements for Building

### Required
- Python 3.7+
- PyInstaller 6.0.0+
- Pillow 10.0.0+ (for asset generation)

### Optional (for installer)
- Inno Setup 6 (https://jrsoftware.org/isdl.php)
- Windows 7 or later

## Advanced Usage

### Custom Asset Generation
```bash
python generate_assets.py
```

### Direct PyInstaller Build
```bash
python build_exe.py
```

### Update Checking
```bash
python -c "from release_manager import UpdateChecker; UpdateChecker('1.2.0').check_github_releases('metinhasimi22/BoxMasterPro')"
```

## Troubleshooting

### Issue: Inno Setup not found
**Solution**: Install Inno Setup from https://jrsoftware.org/isdl.php

### Issue: Icon not displaying
**Solution**: Run `python generate_assets.py` to recreate assets

### Issue: Build fails with "File not found"
**Solution**: Ensure you're running from the project root directory

## GitHub Actions Integration (Optional)

Create `.github/workflows/build.yml` for automated builds:

```yaml
name: Build and Release

on: [push, pull_request]

jobs:
  build:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: 3.9
      - run: pip install -r requirements.txt
      - run: python build_cli.py build --full
      - uses: actions/upload-artifact@v2
        with:
          name: build-artifacts
          path: installer/Output/
```

## Version Numbering

Follows Semantic Versioning (MAJOR.MINOR.PATCH):
- MAJOR: Breaking changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes

Example: `1.2.3`

## Support

For issues or questions:
- GitHub Issues: https://github.com/metinhasimi22/BoxMasterPro/issues
- GitHub Discussions: https://github.com/metinhasimi22/BoxMasterPro/discussions
