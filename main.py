import random
import sys
import math

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QPolygon, QColor


class WindowDraw(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()
        self.setMouseTracking(True)
        self.coord = []
        self.do_paint = False
        self.attr = None

    def paintEvent(self, event):
        if self.do_paint:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def initUI(self):
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle('Супрематизм')
        self.pushButton.clicked.connect(self.paint)
        self.show()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self):
        self.do_paint = False
        const = random.randint(10, 200)
        self.qp.setBrush(QColor(255, 255, 0))
        self.qp.drawEllipse(70, 70, const, const)
        self.qp.drawEllipse(100, 270, const, const)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WindowDraw()
    ex.show()
    sys.exit(app.exec())
