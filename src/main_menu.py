import sys
import time
import webbrowser
import tkinter as tk
from .upload import upload
from .snip_screen import SnipScreen
from PIL import ImageGrab, ImageQt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel
from PyQt5.QtGui import QFont, QPainter, QColor, QBrush, QIcon, QPixmap
from PyQt5.QtCore import Qt, QRect, QPoint, QSize

WIDTH = 400
BORDER_LENGTH = 25
GAP_HEIGHT = 15
MAX_SNIP_HEIGHT = 600
BUTTON_HEIGHT = 100

class MainMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()     
        
    def initUI(self):
        self.setWindowTitle('Snip Uploader')
        self.setFont(QFont('SansSerif', 16))

        self.new_snip_btn()

    def set_window_size(self, height):
        self.setGeometry(100, 100, WIDTH + BORDER_LENGTH * 2, height)
        self.setFixedSize(self.size())
        QApplication.processEvents()

    def new_snip_btn(self):
        snip_btn = QPushButton('New Snip', self)
        snip_btn.resize(WIDTH, BUTTON_HEIGHT)
        snip_btn.move(BORDER_LENGTH, BORDER_LENGTH)
        snip_btn.clicked.connect(self.new_snip_click)

    def new_snip_click(self):
        self.close()
        self.snip_screen = SnipScreen(self)
        self.snip_screen.show()

    def create_upload_btn(self):
        upload_btn = QPushButton('Upload Snip', self)
        upload_btn.resize(WIDTH, BUTTON_HEIGHT)
        upload_btn.move(BORDER_LENGTH, self.total_height)
        upload_btn.clicked.connect(self.upload_btn_click)
        self.upload_btn = upload_btn

    def add_snip_widgets(self, snip, width, h_w_ratio):
        self.snip = snip
        label_height = self.create_snip_label(width, h_w_ratio)
        self.total_height = BORDER_LENGTH + BUTTON_HEIGHT + GAP_HEIGHT + label_height + GAP_HEIGHT
        self.create_upload_btn()

    def add_link_widgets(self, snip, link):
        width, height = snip.size
        self.snip = snip
        self.link = link
        label_height = self.create_snip_label(width, height / width)
        self.total_height = BORDER_LENGTH + BUTTON_HEIGHT + GAP_HEIGHT + label_height + GAP_HEIGHT
        self.create_upload_link()
        self.create_copy_btn(self.total_height + GAP_HEIGHT + BUTTON_HEIGHT)


    def create_upload_link(self):
        upload_btn = QPushButton('Open Link', self)
        upload_btn.resize(WIDTH, BUTTON_HEIGHT)
        upload_btn.move(BORDER_LENGTH, self.total_height)
        upload_btn.clicked.connect(lambda: webbrowser.open(self.link))

    def create_copy_btn(self, height):
        copy_btn = QPushButton('Copy Link', self)
        copy_btn.resize(WIDTH, BUTTON_HEIGHT)
        copy_btn.move(BORDER_LENGTH, height)
        copy_btn.clicked.connect(self.copy_to_clipboard)

    def copy_to_clipboard(self):
        cb = tk.Tk()
        cb.withdraw()
        cb.clipboard_clear()
        cb.clipboard_append(self.link)

    def create_snip_label(self, width, h_w_ratio):
        width = min(width, WIDTH)
        height = min(width * h_w_ratio, MAX_SNIP_HEIGHT)
        width = height / h_w_ratio
        im = self.snip.convert("RGBA")
        qim = ImageQt.ImageQt(im)
        pix = QPixmap.fromImage(qim)
        pix = pix.scaled(width, height)
        snip_label = QLabel(self)
        snip_label.setPixmap(pix)
        snip_label.move(BORDER_LENGTH + (WIDTH - width) / 2, 140)
        snip_label.resize(width, height)
        return height

    def upload_btn_click(self):
        self.upload_btn.hide()
        QApplication.processEvents()
        link = upload(self.snip)

        self.close()
        self.link_menu = MainMenu()
        self.link_menu.add_link_widgets(self.snip, link)
        self.link_menu.show()
        self.link_menu.set_window_size(self.link_menu.total_height + BUTTON_HEIGHT * 2 + GAP_HEIGHT + BORDER_LENGTH)

    def load_snip_info(self, snip, width, h_w_ratio):
        self.snip_menu = MainMenu()
        self.snip_menu.add_snip_widgets(snip, width, h_w_ratio)
        self.snip_menu.show()
        self.snip_menu.set_window_size(self.snip_menu.total_height + BUTTON_HEIGHT + BORDER_LENGTH)

def snip_menu(snip):
    snip_menu = MainMenu()
    snip_menu.add_snip_info(snip)
