# https://iroy123.tistory.com/57

'''
	signal		: event
	slot		: handler
'''

from PyQt5 import QtWidgets

class MyWindows(QtWidgets.QWidget):
    def __init__(self): #생성자를 만들어 줘야한다 
        super().__init__() #부모의 생성자 호출 
        self.setWindowTitle("파이썬 푸시버튼")

        button1 = QtWidgets.QPushButton(self)
        button1.setText("버튼1")

        button2 = QtWidgets.QPushButton(self)
        button2.setText("버튼2")

        # Signal
        #버튼 1, 2를 눌렀을 때 button_clicked라는 함수를 실행 시켜라 시그널
        button1.clicked.connect(self.button_clicked)
        button2.clicked.connect(self.button_clicked)

        #레이아웃에 등록을 해줘야 보인다 
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
        
        self.setLayout(layout)
        self.show()
    
    # Slot
    def button_clicked(self):
        sender = self.sender()
        QtWidgets.QMessageBox.about(self,"버튼테스트",sender.text())
        #sender.text() 시그널의 text를 그대로 출력 

app = QtWidgets.QApplication([])
win = MyWindows()
app.exec_()
