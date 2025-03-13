import os
import importlib.util
from PyQt6.QtWidgets import QMainWindow, QWidget, QGridLayout, QLabel, QVBoxLayout

from pathlib import Path
import sys

import importlib.util
import os
from pathlib import Path

import os, sys

from ANUS.panels.application_list import App, AppList  # Adjust this import to your project structure


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.grid = QGridLayout(self.central_widget)

        plugin_base_dir = sys.path[1]  # Adjust as per your working fix

        categories = [
            ("OS Fixes", "ANUS/plugins/os_fixes_tuneups"),
            ("Setup & Bloatware", "ANUS/plugins/setup_bloatware_removal"),
            ("Virus Removal", "ANUS/plugins/virus_scans"),
            ("Diagnostics", "ANUS/plugins/diagnostics"),
            ("Misc", "ANUS/plugins/misc"),
        ]


        row, col = 0, 0
        for category_name, folder_name in categories:
            apps = scan_plugins(plugin_base=plugin_base(), directory=folder_name)

            if not apps:
                continue

            container_widget = QWidget()
            container_layout = QVBoxLayout(container_widget)

            title_label = QLabel(category_name)
            title_label.setStyleSheet("font-weight: bold; font-size: 16px;")

            app_list_widget = AppList(apps)

            container_layout.addWidget(title_label := QLabel(category_name))
            title_label.setStyleSheet("font-weight: bold; font-size: 16px;")
            container_layout.addWidget(app_list_widget:=AppList(apps))

            self.grid.addWidget(container_widget, row, col)

            col += 1
            if col > 2:
                col = 0
                row += 1


# Helper function to dynamically scan plugins
import importlib.util
from pathlib import Path
import os

def plugin_base():
    import sys
    return sys.path[1]  # your working method


def scan_plugins(plugin_base, directory):
    from pathlib import Path

    full_dir = Path(plugin_base) / directory
    if not full_dir.exists():
        print(f"Directory not found: {full_dir}")
        return []

    apps = []

    for file in full_dir.glob("*.py"):
        module_name = file.stem
        spec = importlib.util.spec_from_file_location(module_name, file)
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
        except Exception as e:
            print(f"Failed to import plugin '{module_name}': {e}")
            continue

        if hasattr(module, "Plugin"):
            plugin_name = getattr(module, "PLUGIN_NAME", module_name)
            plugin_icon = getattr(module, "PLUGIN_ICON", None)

            app = App(plugin_name, plugin_icon, str(file))
            apps.append(app)

    return apps


# Helper function to find the plugin base reliably
def plugin_base():
    return sys.path[1] if len(sys.path) > 1 else os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

