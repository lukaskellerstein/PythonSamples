import sys

from PyQt6 import uic
from PyQt6.QtCore import Qt, pyqtSignal, pyqtSlot
from PyQt6.QtGui import QPainter, QPaintEvent
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

        self.lineEdit.textChanged.connect(self.textChanged)
        self.lineEdit.editingFinished.connect(self.textChangeFinished)

        self.pushButton.clicked.connect(self.doSomething)

    def doSomething(self):
        print("Doing something")
        inputText = self.lineEdit.text()
        print("Input text: " + inputText)
        self.label.setText(inputText)

    @pyqtSlot(str)
    def textChanged(self, text: str):
        print("text " + text)
        self.text = text

    @pyqtSlot()
    def textChangeFinished(self):
        print("Finished with " + self.text)
        # self.on_textChanged.emit(self.text)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
