# example_plugin.py
from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

PLUGIN_NAME = "S-Mode Removal"
PLUGIN_ICON = "path/to/icon.png"

class Plugin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Example Plugin")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Hello from the plugin!"))
        self.setLayout(layout)