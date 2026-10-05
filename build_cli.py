#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""BoxMasterPro Build and Distribution Tool"""

import argparse
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="BoxMasterPro Build and Distribution Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python build_cli.py build            # Build EXE only
  python build_cli.py build --full     # Full production build
  python build_cli.py version bump minor  # Bump minor version
  python build_cli.py release add --version 1.2.0  # Add release
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Build commands
    build_parser = subparsers.add_parser("build", help="Build application")
    build_parser.add_argument(
        "--full", action="store_true", help="Perform full production build"
    )
    build_parser.add_argument(
        "--exe-only", action="store_true", help="Build EXE only"
    )
    build_parser.add_argument(
        "--no-assets", action="store_true", help="Skip asset generation"
    )

    # Version commands
    version_parser = subparsers.add_parser("version", help="Manage version")
    version_parser.add_argument(
        "action", choices=["read", "write", "bump", "info"]
    )
    version_parser.add_argument("--version", help="Version number to set")
    version_parser.add_argument(
        "--part", choices=["major", "minor", "patch"], default="patch"
    )

    # Release commands
    release_parser = subparsers.add_parser("release", help="Manage releases")
    release_parser.add_argument(
        "action", choices=["add", "list", "check", "changelog"]
    )
    release_parser.add_argument("--version", help="Version number")
    release_parser.add_argument("--changelog", help="Changelog text")
    release_parser.add_argument(
        "--repo", default="metinhasimi22/BoxMasterPro", help="GitHub repository"
    )

    # Clean commands
    clean_parser = subparsers.add_parser("clean", help="Clean build artifacts")
    clean_parser.add_argument(
        "--all", action="store_true", help="Remove all build files"
    )

    args = parser.parse_args()

    if args.command == "build":
        handle_build(args)
    elif args.command == "version":
        handle_version(args)
    elif args.command == "release":
        handle_release(args)
    elif args.command == "clean":
        handle_clean(args)
    else:
        parser.print_help()


def handle_build(args):
    """Handle build commands"""
    if args.full:
        from build_production import ProductionBuilder
        builder = ProductionBuilder()
        builder.run_full_build()
    elif args.exe_only:
        from build_production import ProductionBuilder
        builder = ProductionBuilder()
        builder.ensure_directories()
        if not args.no_assets:
            builder.generate_assets()
        builder.build_exe()
    else:
        from build_production import ProductionBuilder
        builder = ProductionBuilder()
        builder.ensure_directories()
        if not args.no_assets:
            builder.generate_assets()
        builder.build_exe()


def handle_version(args):
    """Handle version commands"""
    from version_manager import VersionManager
    manager = VersionManager()

    if args.action == "read":
        print(f"Current version: {manager.read_version()}")
    elif args.action == "write":
        if args.version:
            manager.write_version(args.version)
        else:
            print("✗ Version required")
    elif args.action == "bump":
        manager.bump_version(args.part)
    elif args.action == "info":
        info = manager.get_version_info()
        for key, value in info.items():
            print(f"{key}: {value}")


def handle_release(args):
    """Handle release commands"""
    from release_manager import ReleaseManager, UpdateChecker
    from version import VERSION

    manager = ReleaseManager()

    if args.action == "add":
        if args.version and args.changelog:
            manager.add_release(args.version, args.changelog, [])
        else:
            print("✗ Version and changelog required")
    elif args.action == "list":
        releases = manager.load_releases()
        for release in releases:
            print(f"v{release['version']} ({release['release_date']})")
    elif args.action == "check":
        checker = UpdateChecker(VERSION)
        if checker.check_github_releases(args.repo):
            print(f"✓ Update available: v{checker.latest_version}")
        else:
            print("✓ You are using the latest version")
    elif args.action == "changelog":
        if args.version:
            changelog = manager.generate_changelog(args.version)
            print(changelog if changelog else "✗ Changelog not found")


def handle_clean(args):
    """Handle clean commands"""
    from build_production import ProductionBuilder
    from pathlib import Path
    import shutil

    builder = ProductionBuilder()

    if args.all:
        dirs_to_clean = [
            builder.dist_dir,
            builder.build_dir,
            Path("__pycache__"),
        ]
        for dir_path in dirs_to_clean:
            if dir_path.exists():
                shutil.rmtree(dir_path)
                print(f"✓ Removed {dir_path}")
    else:
        builder.clean_build_artifacts()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠ Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"✗ Error: {e}")
        sys.exit(1)
