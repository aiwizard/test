# https://iroy123.tistory.com/57

from PyQt5 import QtWidgets

class MyWindows(QtWidgets.QWidget):
    def __init__(self): #생성자를 만들어 줘야한다 
        super().__init__() #부모의 생성자 호출 
        self.setWindowTitle("파이썬 푸시버튼")
        button = QtWidgets.QPushButton(self)
        button.setText("일반버튼")

        disableButton = QtWidgets.QPushButton(self)
        disableButton.setText("비활성버튼")
        disableButton.setEnabled(False)

        checkButton = QtWidgets.QPushButton(self)
        checkButton.setText("체크버튼")
        checkButton.setCheckable(True)
        checkButton.toggle()

        #레이아웃에 등록을 해줘야 보인다 
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(button)
        layout.addWidget(disableButton)
        layout.addWidget(checkButton)
        
        self.setLayout(layout)
        self.show()

app = QtWidgets.QApplication([])
win = MyWindows()
app.exec_()

