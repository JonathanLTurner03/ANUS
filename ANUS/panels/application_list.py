from collections import namedtuple

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QMainWindow, QHBoxLayout, QListWidget, QListWidgetItem
from PyQt6.QtGui import QIcon

import importlib.util
import os
import sys


def get_project_root():
    # Adjust if necessary depending on how you're debugging
    return sys.path[1] if hasattr(sys, 'frozen') or sys.path[0].endswith('.zip') else os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))


class App:
    def __init__(self, name, icon, location):
        self.name = name
        self.icon = icon
        self.location = location


class ItemizedApp(QListWidgetItem):
    def __init__(self, app):
        super().__init__(f"(). {app.name}")
        self.location = app.location
        self.name = app.name
        self.icon = app.icon


class AppList(QWidget):
    def __init__(self, list_of_apps):
        super().__init__()

        self.layout = QVBoxLayout()

        self.list = QListWidget()
        for i, app in enumerate(list_of_apps):
            self.list.addItem(ItemizedApp(app))

        self.list.itemDoubleClicked.connect(self.open_app)
        self.layout.addWidget(self.list)
        self.setLayout(self.layout)

    def open_app(self, item):
        base_dir = get_project_root()
        module_path = os.path.normpath(os.path.join(base_dir, item.location))

        # Confirm ".py" is appended if needed
        if not module_path.endswith(".py"):
            module_path += ".py"

        if not os.path.exists(module_path):
            print(f"Plugin file not found: {module_path}")
            return

        module_name = os.path.splitext(os.path.basename(module_path))[0]

        spec = importlib.util.spec_from_file_location(module_name, module_path)
        plugin_module = importlib.util.module_from_spec(spec)

        try:
            spec.loader.exec_module(plugin_module)
        except Exception as e:
            print(f"Error loading plugin '{module_name}': {e}")
            return

        if hasattr(plugin_module, 'Plugin'):
            plugin_class = plugin_module.Plugin
            plugin_instance = plugin_class()

            # Store persistent reference to prevent immediate closure
            if not hasattr(self, 'open_windows'):
                self.open_windows = []
            self.open_windows.append(plugin_instance)

            plugin_instance.show()
        else:
            print(f"No class named 'Plugin' found in '{module_name}'")
