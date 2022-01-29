import sys
import sqlite3
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.connectDataBase()
        self.init_ui()
    def connectDataBase(self):
        connection = sqlite3.connect("database.db")
        self.cursor = connection.cursor()
        self.cursor.execute("Create Table If not exists users (username TEXT, password TEXT)")
        connection.commit()

    def init_ui(self):
        self.username = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login = QtWidgets.QPushButton("Log In")
        self.info = QtWidgets.QLabel("")

        h_box = QtWidgets.QHBoxLayout()
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.username)
        v_box.addWidget(self.password)
        v_box.addWidget(self.info)
        v_box.addStretch()
        v_box.addWidget(self.login)
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)
        self.setWindowTitle("Log In Page")
        self.show()
        self.login.clicked.connect(self.login_func)

    def login_func(self):

        uname = self.username.text()
        passw = self.password.text()

        self.cursor.execute("Select * From users where username = ? and password = ?",(uname,passw))

        data = self.cursor.fetchall()

        if len(data) == 0:
            self.info.setText("There is no such user \nPlease try again.")
        else:
            self.info.setText("Welcome " + uname)






app = QtWidgets.QApplication(sys.argv)

myWindow = Window()

sys.exit(app.exec())