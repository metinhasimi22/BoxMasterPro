import subprocess
import sys
from pathlib import Path

from version import APP_NAME, VERSION


def ensure_assets():
    subprocess.run([sys.executable, "generate_assets.py"], check=True)


def build_exe():
    ensure_assets()
    project_root = Path(__file__).resolve().parent
    main_file = project_root / "main.py"
    icon_file = project_root / "assets" / "boxmaster_icon.ico"
    version_file = project_root / "version_info.txt"

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
        str(main_file),
    ]

    print(f"Building {APP_NAME} {VERSION}...")
    subprocess.run(command, check=True, cwd=str(project_root))


if __name__ == "__main__":
    build_exe()


