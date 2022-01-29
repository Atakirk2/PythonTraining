from PyQt5 import QtWidgets, QtGui
import sys

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.textField = QtWidgets.QLabel("I haven't been clicked")

        self.button = QtWidgets.QPushButton("Click me!")

        self.counter = 0

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.button)
        v_box.addWidget(self.textField)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.button.clicked.connect(self.click)

        self.show()
    def click(self):
        self.counter += 1
        self.textField.setText("I have clicked " + str(self.counter) + " many times!")

app = QtWidgets.QApplication(sys.argv)

myWindow  = Window()

sys.exit(app.exec())