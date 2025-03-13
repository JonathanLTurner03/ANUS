import sys

from PyQt6.QtWidgets import QApplication
from ANUS.views.main_window import MainWindow


def main():
    app = QApplication(sys.argv)

    # Initialize the main window
    main_window = MainWindow()
    screen_size = app.primaryScreen().size()
    main_window.resize(int(screen_size.width()/3), int(screen_size.height()/5))
    main_window.setWindowTitle("ANUS - Analysis, Nixing, Upkeep, & Security")
    #main_window.setWindowIcon(QIcon("resources/icons/Icarus Icon.ico"))

    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
