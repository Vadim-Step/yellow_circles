import random
import sys
import math

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QPolygon, QColor
from UI import Ui_MainWindow


class WindowDraw(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()
        self.setMouseTracking(True)
        self.coord = []
        self.setupUi(self)
        self.do_paint = False
        self.attr = None
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def initUI(self):
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle('Супрематизм')

        self.show()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw(self):
        self.do_paint = False
        const = random.randint(10, 200)
        mass = [i for i in range(0, 256)]
        self.qp.setBrush(QColor(random.choice(mass), random.choice(mass), random.choice(mass)))
        self.qp.drawEllipse(70, 70, const, const)
        self.qp.drawEllipse(100, 270, const, const)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WindowDraw()
    ex.show()
    sys.exit(app.exec())
