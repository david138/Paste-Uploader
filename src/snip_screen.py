import sys
import tkinter as tk
from PIL import ImageGrab
from .upload import upload
from .upload_info import UploadInfo
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QFont, QPainter, QColor, QBrush
from PyQt5.QtCore import Qt, QRect, QPoint

class SnipScreen(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()     
        
    def initUI(self):
        root = tk.Tk()
        self.screen_w = root.winfo_screenwidth()
        self.screen_h = root.winfo_screenheight()
        self.setGeometry(0, 0, self.screen_w, self.screen_h)
        self.x = 0
        self.y = 0
        self.offset_x = 0
        self.offset_y = 0

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        self.setCursor(Qt.CrossCursor)
        self.show()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()

    def drawRectangles(self, qp):
        self.drawSurroundingSquares(qp)
        self.drawBorder(qp)
        self.drawSelectRectangle(qp)

    def drawSelectRectangle(self, qp):
        qp.setPen(Qt.NoPen)
        qp.setPen(QColor(Qt.red))
        qp.setBrush(QColor(255, 255, 255))
        qp.setOpacity(0.01)
        qp.drawRect(self.x, self.y, self.offset_x, self.offset_y)

    def drawBorder(self, qp):
        qp.setPen(QColor(Qt.red))
        qp.setPen(QColor(Qt.red))
        qp.setBrush(QColor(255, 255, 255))
        qp.setOpacity(1)
        qp.drawRect(self.x, self.y, 1, self.offset_y) # left
        qp.drawRect(self.x + self.offset_x - 1, self.y, 1, self.offset_y) # right
        qp.drawRect(self.x, self.y, self.offset_x, 1) # top
        qp.drawRect(self.x, self.y + self.offset_y - 1, self.offset_x, 1) # bot

    def drawSurroundingSquares(self, qp):
        right_edge = self.x + self.offset_x
        bottom_edge = self.y + self.offset_y

        qp.setPen(Qt.NoPen)
        qp.setBrush(QColor(Qt.white))
        qp.setOpacity(0.2)
        qp.drawRect(0, self.y, self.x, self.offset_y)  # left
        qp.drawRect(right_edge, self.y, self.screen_w - right_edge, self.offset_y) # right
        qp.drawRect(0, 0, self.screen_w, self.y) # top
        qp.drawRect(0, bottom_edge, self.screen_w, self.screen_h - bottom_edge) # bottom

    def mousePressEvent(self, event):
        self.origin = event.pos()
        self.x = self.origin.x()
        self.y = self.origin.y()
        self.offset_x = 0
        self.offset_y = 0
        self.update()

    def mouseMoveEvent(self, event):
        cur_x = event.pos().x()
        cur_y = event.pos().y()

        if cur_x >= self.origin.x():
            self.x = self.origin.x()
            self.offset_x = cur_x - self.x
        else:
            self.x = cur_x
            self.offset_x = self.origin.x() - cur_x

        if cur_y >= self.origin.y():
            self.y = self.origin.y()
            self.offset_y = cur_y - self.y
        else:
            self.y = cur_y
            self.offset_y = self.origin.y() - cur_y
        self.update()

    def mouseReleaseEvent(self, event):
        self.close()
        self.upload_image()

    def upload_image(self):
        link = upload(ImageGrab.grab((self.x, self.y, self.x + self.offset_x, self.y + self.offset_y)))
        self.upload_info = UploadInfo(link)
        self.upload_info.show()


def snip_screen():
    app = QApplication(sys.argv)
    snip_screen = SnipScreen()
    sys.exit(app.exec_())
    
