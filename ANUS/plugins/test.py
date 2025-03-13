from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QLabel
from ANUS.panels.application_list import App, AppList

class Plugin(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QHBoxLayout(self.central_widget)

        app_list = {
            App("test1", None, "ANUS/views/main_window"),
            App("test2", None, "bigBob"),
            App("test3", None, "bigBob"),
            App("test4", None, "bigBob")
        }

        frequent = AppList(app_list)

        layout.addWidget(frequent)