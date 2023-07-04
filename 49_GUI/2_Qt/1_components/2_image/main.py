import sys

from PyQt6 import uic
from PyQt6.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt6.QtGui import QPainter, QPaintEvent, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget


class MainWindow(QMainWindow):
    text: str = ""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        # load template
        uic.loadUi("main.ui", self)

        # load styles
        with open("main.qss", "r") as fh:
            self.setStyleSheet(fh.read())

        self.label.setPixmap(QPixmap("dog.jpg"))
        self.label.setScaledContents(True)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
