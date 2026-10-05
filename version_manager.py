import os
import sys
from pathlib import Path


class VersionManager:
    def __init__(self, version_file="VERSION"):
        self.version_file = Path(version_file)

    def read_version(self):
        """Read version from file"""
        if self.version_file.exists():
            return self.version_file.read_text().strip()
        return "0.0.0"

    def write_version(self, version):
        """Write version to file"""
        self.version_file.write_text(version.strip())
        print(f"✓ Version updated to {version}")

    def bump_version(self, part="patch"):
        """Bump version number"""
        version = self.read_version()
        parts = version.split(".")
        if len(parts) != 3:
            print("✗ Invalid version format")
            return False

        major, minor, patch = map(int, parts)

        if part == "major":
            major += 1
            minor = 0
            patch = 0
        elif part == "minor":
            minor += 1
            patch = 0
        elif part == "patch":
            patch += 1
        else:
            print("✗ Invalid part. Use 'major', 'minor', or 'patch'")
            return False

        new_version = f"{major}.{minor}.{patch}"
        self.write_version(new_version)
        return True

    def get_version_info(self):
        """Get detailed version information"""
        version = self.read_version()
        return {
            "version": version,
            "python": sys.version,
            "platform": sys.platform,
        }


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Version Manager for BoxMasterPro")
    parser.add_argument(
        "command", choices=["read", "write", "bump", "info"], help="Command to execute"
    )
    parser.add_argument(
        "--version", help="Version to set (for write command)"
    )
    parser.add_argument(
        "--part", choices=["major", "minor", "patch"], default="patch",
        help="Version part to bump (for bump command)"
    )

    args = parser.parse_args()
    manager = VersionManager()

    if args.command == "read":
        print(f"Current version: {manager.read_version()}")
    elif args.command == "write":
        if args.version:
            manager.write_version(args.version)
        else:
            print("✗ Version required for write command")
    elif args.command == "bump":
        manager.bump_version(args.part)
    elif args.command == "info":
        info = manager.get_version_info()
        for key, value in info.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()
