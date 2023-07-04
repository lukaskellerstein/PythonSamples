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

        self.checkBox1.setCheckState(Qt.CheckState.Checked)
        self.checkBox1.stateChanged.connect(self.checkbox1Changed)

        # self.radioButton1.setChecked(True)
        self.radioButton1.clicked.connect(self.radio1Changed)
        self.radioButton2.clicked.connect(self.radio2Changed)

    @pyqtSlot(int)
    def checkbox1Changed(self, state):
        print("Checkbox 1 changed to " + str(state))
        self.labelText1.setVisible(state / 2 == 1)

    @pyqtSlot(bool)
    def radio1Changed(self, state):
        print("Radio 1 changed to " + str(state))
        self.labelText3.setVisible(True)

    @pyqtSlot(bool)
    def radio2Changed(self, state):
        print("Radio 2 changed to " + str(state))
        self.labelText3.setVisible(False)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
