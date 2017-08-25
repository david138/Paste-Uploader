import sys
from .main_menu import MainMenu
from PyQt5.QtWidgets import QWidget, QApplication

def start_app_loop():
    app = QApplication(sys.argv)
    main_menu = MainMenu()
    main_menu.show()
    sys.exit(app.exec_())
    