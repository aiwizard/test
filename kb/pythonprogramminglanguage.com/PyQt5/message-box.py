# https://pythonprogramminglanguage.com/pyqt5-message-box/

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QSize    

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(300, 300))    
        self.setWindowTitle("PyQt messagebox example - pythonprogramminglanguage.com") 

        pybutton = QPushButton('Show messagebox', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,64)
        pybutton.move(50, 50)

        pybutton2 = QPushButton('Show messagebox2', self)
        pybutton2.clicked.connect(self.clickMethod2)
        pybutton2.resize(200,64)
        pybutton2.move(50, 120)

    def clickMethod(self):
        QMessageBox.about(self, "Title", "Message")

    def clickMethod2(self):
        ret = QMessageBox.question(self, 'MessageBox', "Click a button", QMessageBox.Ok | QMessageBox.Cancel)

        if ret == QMessageBox.Ok:
            print('Button QMessageBox.Ok clicked.')
        else:
            print('Button QMessageBox.Cancel clicked')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )