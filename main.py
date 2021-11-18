import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget
from random import randint

class Yellow_circle_wid(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.setFixedSize(300, 460)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Рисование')
        self.do_paint = False
        self.drw.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        k = randint(30, 120)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(120, 140, k, k)
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Yellow_circle_wid()
    ex.show()
    sys.exit(app.exec())
