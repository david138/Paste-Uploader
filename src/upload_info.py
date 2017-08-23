import sys
import tkinter as tk
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QFont, QPainter, QColor, QBrush
from PyQt5.QtCore import Qt, QRect, QPoint

class UploadInfo(QWidget):
    def __init__(self, link):
        super().__init__()
        self.initUI(link)     
        
    def initUI(self, link):
        root = tk.Tk()
        self.screen_w = root.winfo_screenwidth()
        self.screen_h = root.winfo_screenheight()
        self.setGeometry(self.screen_w - 400, self.screen_h - 200, 400, 200)
        self.setWindowTitle('Snip Uploaded')

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        link_button = QPushButton(link, self)
        link_button.resize(200, 40)
        link_button.move(100,80)

