import sys

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget

class Yellow_circle_wid(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Yellow_circle_wid()
    ex.show()
    sys.exit(app.exec())
