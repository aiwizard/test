# https://pythonprogramminglanguage.com/pyqt5-button/

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(320, 140))    
        self.setWindowTitle("PyQt Line Edit example (textfield) - pythonprogramminglanguage.com") 

        # QLabel
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Name:')
        self.nameLabel.move(20, 20)

        # QLineEdit
        self.line = QLineEdit(self)
        self.line.setToolTip('Input name here')
        self.line.resize(200, 32)
        self.line.move(80, 20)

 		  # QPushButton
        pybutton = QPushButton('OK', self)
        pybutton.setToolTip('This is a tooltip message.')
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,32)
        pybutton.move(80, 60)        

    def clickMethod(self):
        print('Your name: ' + self.line.text())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )
