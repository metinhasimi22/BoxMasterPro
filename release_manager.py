import os
import sys
import json
from pathlib import Path
from datetime import datetime


class ReleaseManager:
    def __init__(self):
        self.releases_dir = Path("releases")
        self.releases_dir.mkdir(exist_ok=True)
        self.releases_file = self.releases_dir / "releases.json"

    def load_releases(self):
        """Load release history"""
        if self.releases_file.exists():
            with open(self.releases_file, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def save_releases(self, releases):
        """Save release history"""
        with open(self.releases_file, "w", encoding="utf-8") as f:
            json.dump(releases, f, indent=2, ensure_ascii=False)

    def add_release(self, version, changelog, assets):
        """Add a new release"""
        releases = self.load_releases()
        release = {
            "version": version,
            "release_date": datetime.now().isoformat(),
            "changelog": changelog,
            "assets": assets,
            "download_count": 0,
        }
        releases.append(release)
        self.save_releases(releases)
        print(f"✓ Release v{version} added to history")

    def get_latest_release(self):
        """Get latest release"""
        releases = self.load_releases()
        return releases[-1] if releases else None

    def generate_changelog(self, version):
        """Generate changelog for a version"""
        changelog_file = self.releases_dir / f"CHANGELOG_v{version}.md"
        if changelog_file.exists():
            return changelog_file.read_text()
        return ""


class UpdateChecker:
    """Check for application updates"""

    def __init__(self, current_version):
        self.current_version = current_version
        self.latest_version = None

    def check_github_releases(self, repo):
        """Check GitHub releases for newer version"""
        try:
            import urllib.request
            url = f"https://api.github.com/repos/{repo}/releases/latest"
            with urllib.request.urlopen(url, timeout=5) as response:
                data = json.loads(response.read().decode())
                self.latest_version = data.get("tag_name", "").lstrip("v")
                return self.is_update_available()
        except Exception as e:
            print(f"⚠ Could not check for updates: {e}")
            return False

    def is_update_available(self):
        """Check if update is available"""
        if not self.latest_version:
            return False
        return self._compare_versions(self.current_version, self.latest_version) < 0

    @staticmethod
    def _compare_versions(v1, v2):
        """Compare two versions. Returns -1 if v1 < v2, 0 if equal, 1 if v1 > v2"""
        v1_parts = [int(x) for x in v1.split(".")]
        v2_parts = [int(x) for x in v2.split(".")]

        for i in range(max(len(v1_parts), len(v2_parts))):
            v1_part = v1_parts[i] if i < len(v1_parts) else 0
            v2_part = v2_parts[i] if i < len(v2_parts) else 0

            if v1_part < v2_part:
                return -1
            elif v1_part > v2_part:
                return 1

        return 0


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Release Manager for BoxMasterPro")
    parser.add_argument("command", choices=["add", "list", "check", "changelog"])
    parser.add_argument("--version", help="Version number")
    parser.add_argument("--repo", default="metinhasimi22/BoxMasterPro", help="GitHub repository")
    parser.add_argument("--changelog", help="Changelog text")

    args = parser.parse_args()
    manager = ReleaseManager()

    if args.command == "add":
        if args.version and args.changelog:
            manager.add_release(args.version, args.changelog, [])
        else:
            print("✗ Version and changelog required")
    elif args.command == "list":
        releases = manager.load_releases()
        for release in releases:
            print(f"v{release['version']} ({release['release_date']})")
    elif args.command == "check":
        from version import VERSION
        checker = UpdateChecker(VERSION)
        if checker.check_github_releases(args.repo):
            print(f"✓ Update available: v{checker.latest_version}")
        else:
            print("✓ You are using the latest version")
    elif args.command == "changelog":
        if args.version:
            changelog = manager.generate_changelog(args.version)
            print(changelog if changelog else "✗ Changelog not found")


if __name__ == "__main__":
    main()
