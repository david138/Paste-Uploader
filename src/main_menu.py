import sys
import tkinter as tk
from .upload import upload
from .snip_screen import SnipScreen
from PIL import ImageGrab, ImageQt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from PyQt5.QtGui import QFont, QPainter, QColor, QBrush, QIcon, QPixmap
from PyQt5.QtCore import Qt, QRect, QPoint, QSize

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()     
        
    def initUI(self):
        self.setWindowTitle('Snip Uploader')
        self.setGeometry(100, 100, 400, 600)
        self.setFont(QFont('SansSerif', 16))

        self.new_snip_btn()

    def new_snip_btn(self):
        snip_btn = QPushButton('New Snip', self)
        snip_btn.resize(300, 75)
        snip_btn.move(50, 50)
        snip_btn.clicked.connect(self.new_snip_click)

    def new_snip_click(self):
        self.close()
        self.snip_screen = SnipScreen(self)
        self.snip_screen.show()

    def create_upload_btn(self):
        upload_btn = QPushButton('Upload Snip', self)
        upload_btn.resize(300, 75)
        upload_btn.move(50, 350)
        upload_btn.clicked.connect(self.upload_btn_click)
        self.upload_btn = upload_btn

    def add_snip_widgets(self, snip):
        self.snip = snip
        self.create_snip_label()
        self.create_upload_btn()
        self.create_uploading_label()
        self.create_upload_link()
        self.create_copy_btn()

    def create_uploading_label(self):
        loading_label = QLabel(self)
        loading_label.setText('Uploading...')
        loading_label.resize(300, 75)
        loading_label.move(50,350)
        loading_label.hide()
        self.loading_label = loading_label

    def create_upload_link(self):
        link_label = QLabel(self)
        link_label.setOpenExternalLinks(True)
        link_label.setText('')
        link_label.resize(300, 75)
        link_label.move(125,350)
        link_label.hide()
        self.link_label = link_label

    def create_copy_btn(self):
        copy_btn = QPushButton('', self)
        copy_btn.resize(50, 50)
        copy_btn.move(175, 425)
        copy_btn.setIcon(QIcon('res/copy_icon.jpg'))
        copy_btn.setIconSize(QSize(44,44))
        copy_btn.clicked.connect(self.copy_to_clipboard)
        copy_btn.hide()
        self.copy_btn = copy_btn

    def copy_to_clipboard(self):
        cb = tk.Tk()
        cb.withdraw()
        cb.clipboard_clear()
        cb.clipboard_append(self.link)

    def create_snip_label(self):
        im = self.snip.convert("RGBA")
        qim = ImageQt.ImageQt(im)
        pix = QPixmap.fromImage(qim)
        pix = pix.scaled(350, 200)
        snip_label = QLabel(self)
        snip_label.setPixmap(pix)
        snip_label.move(25, 140)
        snip_label.resize(350, 200)
        self.update()

    def upload_btn_click(self):
        self.upload_btn.hide()
        self.loading_label.show()
        self.link = upload(self.snip)
        self.loading_label.hide()

        self.link_label.setText('<a href="' + self.link + '">Snip Uploaded</a>')
        self.link_label.show()
        self.copy_btn.show()

    def load_snip_info(self, snip):
        self.snip_menu = MainMenu()
        self.snip_menu.add_snip_widgets(snip)
        self.snip_menu.show()

def snip_menu(snip):
    snip_menu = MainMenu()
    snip_menu.add_snip_info(snip)

