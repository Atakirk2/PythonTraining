import sys
import os

from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout,QFileDialog,QHBoxLayout

from PyQt5.QtWidgets import QAction,qApp,QMainWindow

class Notepad(QWidget):
    def __init__(self):

        super().__init__()

        self.init_ui()
    def init_ui(self):

        self.textField = QTextEdit()

        self.clearText = QPushButton("Clear")
        self.open = QPushButton("Open")
        self.save = QPushButton("Save")

        h_box = QHBoxLayout()

        h_box.addWidget(self.clearText)
        h_box.addWidget(self.open)
        h_box.addWidget(self.save)

        v_box = QVBoxLayout()

        v_box.addWidget(self.textField)

        v_box.addLayout(h_box)

        self.setLayout(v_box)

        self.setWindowTitle("NotePad")
        self.clearText.clicked.connect(self.clear_text)
        self.open.clicked.connect(self.open_file)
        self.save.clicked.connect(self.save_file)




    def clear_text(self):
        self.textField.clear()

    def open_file(self):
        fileName = QFileDialog.getOpenFileName(self,"Open File",os.getenv("HOME"))

        with open(fileName[0],"r") as file:
            self.textField.setText(file.read())

    def save_file(self):
        fileName = QFileDialog.getSaveFileName(self,"Save File",os.getenv("HOME"))

        with open(fileName[0],"w") as file:

            file.write(self.textField.toPlainText())

class Menu(QMainWindow):

    def __init__(self):

        super().__init__()


        self.window = Notepad()

        self.setCentralWidget(self.window)


        self.init_menu()
    def init_menu(self):

        menubar = self.menuBar()

        file = menubar.addMenu("File")

        open_file = QAction("Open File",self)
        open_file.setShortcut("Ctrl+O")

        save_file = QAction("Save File",self)

        save_file.setShortcut("Ctrl+S")

        clearAll = QAction("Clear File",self)
        clearAll.setShortcut("Ctrl+D")

        exit = QAction("Exit",self)

        exit.setShortcut("Ctrl+Q")

        file.addAction(open_file)
        file.addAction(save_file)
        file.addAction(clearAll)
        file.addAction(exit)

        file.triggered.connect(self.response)


        self.setWindowTitle("Atakirk's Text Editor")

        self.show()

    def response(self,action):

        if action.text() == "Open File":
            self.window.open_file()

        elif action.text() == "Save File":
            self.window.save_file()
        elif action.text() == "Clear File":
            self.window.clear_text()

        elif action.text() == "Exit":
            qApp.quit()




app = QApplication(sys.argv)

menu = Menu()


sys.exit(app.exec_())