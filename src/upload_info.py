import sys
import tkinter as tk
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from PyQt5.QtGui import QFont, QPainter, QColor, QBrush, QIcon, QPixmap
from PyQt5.QtCore import Qt, QRect, QPoint, QSize

class UploadInfo(QWidget):
    def __init__(self, link):
        super().__init__()
        self.link = link
        self.initUI()     
        
    def initUI(self):
        root = tk.Tk()
        self.screen_w = root.winfo_screenwidth()
        self.screen_h = root.winfo_screenheight()
        self.setGeometry(self.screen_w - 400, self.screen_h - 200, 400, 200)
        self.setWindowTitle('Snip Uploaded')

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        self.create_link()
        self.create_copy()

    def create_link(self):
        self.setFont(QFont('SansSerif', 14))
        link_label = QLabel(self)
        link_label.setOpenExternalLinks(True)
        link_label.setText('<a href="' + self.link + '">Snip Uploaded</a>')
        link_label.resize(200, 40)
        link_label.move(100,80)

    def create_copy(self):
        copy_button = QPushButton('', self)
        copy_button.resize(50, 50)
        copy_button.move(235, 70)
        copy_button.setIcon(QIcon('res/copy_icon.jpg'))
        copy_button.setIconSize(QSize(44,44))
        copy_button.clicked.connect(self.on_click)

    def on_click(self, link):
        cb = tk.Tk()
        cb.withdraw()
        cb.clipboard_clear()
        cb.clipboard_append(self.link)