# https://pythonprogramminglanguage.com/pyqt-combobox/
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QComboBox
from PyQt5.QtCore import QSize, QRect    

class ExampleWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(640, 140))    
        self.setWindowTitle("Combobox example") 

        centralWidget = QWidget(self)          
        self.setCentralWidget(centralWidget)   

        # Create combobox and add items.
        self.comboBox = QComboBox(centralWidget)
        self.comboBox.setGeometry(QRect(40, 40, 491, 31))
        self.comboBox.setObjectName(("comboBox"))
        self.comboBox.addItem("PyQt")
        self.comboBox.addItem("Qt")
        self.comboBox.addItem("Python")
        self.comboBox.addItem("Example")
        self.comboBox.addItem("-------------")

        options = ["Athens","Bruxelles","Chengmai","Dover"]
        for option in options:
            self.comboBox.addItem(option)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = ExampleWindow()
    mainWin.show()
    sys.exit( app.exec_() )