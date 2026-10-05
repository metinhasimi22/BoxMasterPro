import tkinter as tk
from tkinter import messagebox
import os
from version import VERSION


class UpdateNotifier:
    """Notify user about available updates"""

    def __init__(self, root, current_version):
        self.root = root
        self.current_version = current_version
        self.update_available = False

    def show_update_dialog(self, new_version, download_url):
        """Show update notification dialog"""
        message = f"""Yeni versiyon kullanılabilir!

Mevcut: v{self.current_version}
Yeni: v{new_version}

Güncellemek istiyorsanız, aşağıdaki bağlantıyı ziyaret edin:
{download_url}
        """

        result = messagebox.showinfo(
            "BoxMasterPro Güncellemesi",
            message,
            icon=messagebox.INFO
        )
        return result

    def check_for_updates_async(self, repo="metinhasimi22/BoxMasterPro"):
        """Check for updates in background (non-blocking)"""
        try:
            from release_manager import UpdateChecker
            checker = UpdateChecker(self.current_version)
            if checker.check_github_releases(repo):
                self.update_available = True
                return checker.latest_version
        except Exception:
            pass
        return None


class AppTrayIcon:
    """System tray icon for BoxMasterPro (Windows only)"""

    def __init__(self, root, app_name="BoxMasterPro"):
        self.root = root
        self.app_name = app_name
        self.try_create_tray_icon()

    def try_create_tray_icon(self):
        """Attempt to create system tray icon"""
        try:
            if os.name == "nt":
                try:
                    from pystray import Icon, Menu, MenuItem
                    from PIL import Image, ImageDraw
                    
                    image = Image.new('RGB', (64, 64), color='#0f172a')
                    ImageDraw.Draw(image).ellipse([(8, 8), (56, 56)], fill='#f97316')
                    
                    menu = Menu(
                        MenuItem('Show', self._show_window),
                        MenuItem('Exit', self._exit_app)
                    )
                    
                    self.icon = Icon(self.app_name, image, menu=menu)
                except ImportError:
                    pass
        except Exception:
            pass

    def _show_window(self, icon, item):
        self.root.deiconify()
        self.root.lift()

    def _exit_app(self, icon, item):
        icon.stop()
        self.root.quit()


class AppManifest:
    """Application manifest and metadata"""

    MANIFEST = {
        "app_name": "BoxMasterPro",
        "version": VERSION,
        "author": "Metino",
        "description": "Professional boxing training assistant with dark mode UI",
        "license": "MIT",
        "repository": "https://github.com/metinhasimi22/BoxMasterPro",
        "homepage": "https://github.com/metinhasimi22/BoxMasterPro",
        "minimum_windows_version": "7",
        "requires_internet": False,
        "auto_start": False,
        "system_tray": True,
        "update_check_interval": 7,  # days
    }

    @classmethod
    def get_manifest(cls):
        return cls.MANIFEST

    @classmethod
    def get_version(cls):
        return cls.MANIFEST["version"]

    @classmethod
    def get_app_name(cls):
        return cls.MANIFEST["app_name"]


if __name__ == "__main__":
    print("Application Manifest:")
    for key, value in AppManifest.get_manifest().items():
        print(f"  {key}: {value}")
