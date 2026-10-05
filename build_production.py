import json
import os
import subprocess
import sys
from pathlib import Path
from datetime import datetime

from version import APP_NAME, VERSION


class ProductionBuilder:
    def __init__(self):
        self.project_root = Path(__file__).resolve().parent
        self.dist_dir = self.project_root / "dist"
        self.build_dir = self.project_root / "build"
        self.installer_dir = self.project_root / "installer"
        self.output_dir = self.installer_dir / "Output"
        self.assets_dir = self.project_root / "assets"

    def ensure_directories(self):
        """Create all necessary directories"""
        for directory in [self.dist_dir, self.build_dir, self.installer_dir, self.output_dir, self.assets_dir]:
            directory.mkdir(exist_ok=True, parents=True)
        print("✓ Directories created")

    def generate_assets(self):
        """Generate application icon and splash screen"""
        print("\n📦 Generating assets...")
        result = subprocess.run([sys.executable, "generate_assets.py"], cwd=str(self.project_root))
        if result.returncode == 0:
            print("✓ Assets generated successfully")
        else:
            print("✗ Failed to generate assets")
            return False
        return True

    def build_exe(self):
        """Build Windows EXE using PyInstaller"""
        print("\n🔨 Building Windows EXE...")
        main_file = self.project_root / "main.py"
        icon_file = self.assets_dir / "boxmaster_icon.ico"
        version_file = self.project_root / "version_info.txt"

        command = [
            sys.executable,
            "-m",
            "PyInstaller",
            "--onefile",
            "--windowed",
            "--name",
            APP_NAME,
            "--icon",
            str(icon_file),
            "--version-file",
            str(version_file),
            "--add-data",
            f"{self.assets_dir}{os.pathsep}assets",
            str(main_file),
        ]

        result = subprocess.run(command, cwd=str(self.project_root))
        if result.returncode == 0:
            print(f"✓ EXE built successfully: {self.dist_dir / f'{APP_NAME}.exe'}")
            return True
        else:
            print("✗ Failed to build EXE")
            return False

    def create_installer(self):
        """Create Windows installer using Inno Setup"""
        print("\n📋 Creating Windows installer...")
        iss_file = self.installer_dir / "BoxMasterPro.iss"

        if not iss_file.exists():
            print("✗ Inno Setup script not found")
            return False

        inno_setup_path = self._find_inno_setup()
        if not inno_setup_path:
            print("✗ Inno Setup not found. Please install Inno Setup from https://jrsoftware.org/isdl.php")
            return False

        command = [str(inno_setup_path), str(iss_file)]
        result = subprocess.run(command, cwd=str(self.project_root))
        if result.returncode == 0:
            print(f"✓ Installer created successfully: {self.output_dir / 'BoxMasterPro-Setup.exe'}")
            return True
        else:
            print("✗ Failed to create installer")
            return False

    @staticmethod
    def _find_inno_setup():
        """Find Inno Setup installation path"""
        common_paths = [
            Path("C:/Program Files (x86)/Inno Setup 6/ISCC.exe"),
            Path("C:/Program Files/Inno Setup 6/ISCC.exe"),
            Path("C:/Program Files (x86)/Inno Setup 5/ISCC.exe"),
            Path("C:/Program Files/Inno Setup 5/ISCC.exe"),
        ]

        for path in common_paths:
            if path.exists():
                return path
        return None

    def create_portable_zip(self):
        """Create portable ZIP package"""
        print("\n📦 Creating portable ZIP...")
        import shutil

        exe_file = self.dist_dir / f"{APP_NAME}.exe"
        if not exe_file.exists():
            print("✗ EXE file not found")
            return False

        zip_name = f"{APP_NAME}-{VERSION}-portable"
        zip_path = self.installer_dir / "Output" / zip_name

        try:
            shutil.make_archive(str(zip_path), "zip", self.dist_dir)
            print(f"✓ Portable ZIP created: {zip_path}.zip")
            return True
        except Exception as e:
            print(f"✗ Failed to create ZIP: {e}")
            return False

    def create_release_notes(self):
        """Generate release notes"""
        print("\n📝 Generating release notes...")
        release_notes_path = self.installer_dir / "Output" / f"RELEASE_NOTES_v{VERSION}.txt"

        release_notes = f"""BoxMasterPro v{VERSION}
Release Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

=== New Features ===
- Modern dark UI with Tkinter
- Random punch combination generator
- Round and rest timer management
- Audio alerts for work/rest transitions
- Automatic version tracking
- Windows installer support
- Portable ZIP distribution
- Production-ready packaging

=== System Requirements ===
- Windows 7 or later
- 50 MB free disk space
- No additional dependencies required

=== Installation ===
1. Download BoxMasterPro-Setup.exe
2. Double-click the installer
3. Follow the setup wizard
4. Launch from Start Menu or Desktop shortcut

=== Portable Version ===
1. Extract BoxMasterPro-{VERSION}-portable.zip
2. Run BoxMasterPro.exe directly
3. No installation required

=== Uninstallation ===
- Use Windows Add/Remove Programs
- Or run the uninstaller from Program Files

=== Support ===
For issues or feedback, visit: https://github.com/metinhasimi22/BoxMasterPro
"""

        try:
            release_notes_path.write_text(release_notes, encoding="utf-8")
            print(f"✓ Release notes created: {release_notes_path}")
            return True
        except Exception as e:
            print(f"✗ Failed to create release notes: {e}")
            return False

    def create_build_manifest(self):
        """Create build manifest for version tracking"""
        print("\n📋 Creating build manifest...")
        manifest = {
            "app_name": APP_NAME,
            "version": VERSION,
            "build_date": datetime.now().isoformat(),
            "python_version": sys.version,
            "platform": sys.platform,
            "files": {
                "exe": str(self.dist_dir / f"{APP_NAME}.exe"),
                "installer": str(self.output_dir / "BoxMasterPro-Setup.exe"),
                "portable_zip": str(self.output_dir / f"{APP_NAME}-{VERSION}-portable.zip"),
            },
        }

        manifest_path = self.installer_dir / "Output" / "build_manifest.json"
        try:
            with open(manifest_path, "w", encoding="utf-8") as f:
                json.dump(manifest, f, indent=2)
            print(f"✓ Build manifest created: {manifest_path}")
            return True
        except Exception as e:
            print(f"✗ Failed to create manifest: {e}")
            return False

    def clean_build_artifacts(self):
        """Clean up build artifacts"""
        print("\n🧹 Cleaning up build artifacts...")
        import shutil

        artifacts = [self.build_dir, self.project_root / f"{APP_NAME}.spec"]
        for artifact in artifacts:
            try:
                if artifact.is_dir():
                    shutil.rmtree(artifact)
                elif artifact.is_file():
                    artifact.unlink()
            except Exception as e:
                print(f"⚠ Could not remove {artifact}: {e}")

        print("✓ Build artifacts cleaned")

    def run_full_build(self):
        """Run complete production build pipeline"""
        print(f"\n{'='*60}")
        print(f"🚀 BoxMasterPro v{VERSION} - Production Build")
        print(f"{'='*60}\n")

        steps = [
            ("Create directories", self.ensure_directories),
            ("Generate assets", self.generate_assets),
            ("Build EXE", self.build_exe),
            ("Create installer", self.create_installer),
            ("Create portable ZIP", self.create_portable_zip),
            ("Generate release notes", self.create_release_notes),
            ("Create build manifest", self.create_build_manifest),
            ("Clean artifacts", self.clean_build_artifacts),
        ]

        for step_name, step_func in steps:
            try:
                if not step_func():
                    print(f"\n⚠ Build continued despite issues in: {step_name}")
            except Exception as e:
                print(f"\n✗ Error in {step_name}: {e}")

        print(f"\n{'='*60}")
        print(f"✓ Production build complete!")
        print(f"{'='*60}")
        print(f"\n📍 Output location: {self.output_dir}")
        print(f"   - BoxMasterPro.exe (EXE only)")
        print(f"   - BoxMasterPro-Setup.exe (Installer)")
        print(f"   - BoxMasterPro-{VERSION}-portable.zip (Portable)")
        print(f"   - RELEASE_NOTES_v{VERSION}.txt")
        print(f"   - build_manifest.json")


def main():
    builder = ProductionBuilder()
    try:
        builder.run_full_build()
    except KeyboardInterrupt:
        print("\n\n⚠ Build interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
