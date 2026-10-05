import subprocess
import sys
from pathlib import Path


def build_exe():
    project_root = Path(__file__).resolve().parent
    main_file = project_root / "main.py"

    command = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--onefile",
        "--windowed",
        "--name",
        "BoxMasterPro",
        str(main_file),
    ]

    print("Building Windows executable...")
    subprocess.run(command, check=True, cwd=str(project_root))


if __name__ == "__main__":
    build_exe()
