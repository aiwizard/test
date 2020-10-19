# https://iroy123.tistory.com/57

from PyQt5 import QtWidgets
# QtWidgets.QLineEdit 이렇게 쓰거나 

#from PyQt5.QtWidgets import QLabel,QLineEdit #필요한 라이브러리를 불러와야함 
# QLineEdit 이렇게 쓰거나 

#from PyQt5.QtWidgets import * #권장하는 방식이 아님 

from PyQt5 import QtCore

class MyWindows(QtWidgets.QWidget):
    def __init__(self): #생성자를 만들어 줘야한다 
        super().__init__() #부모의 생성자 호출 
        self.setWindowTitle("파이썬 지유아이")

        label1 = QtWidgets.QLabel("라벨 1입니다 라벨의 이름을 적어준다 ",self)
        #mysindows라는 클래스에서 사용 되고이쓴 label을 사용해야하기 때문에 부모의 라벨을 불러오기 위해서 self로 되어있다 
        label1.setAlignment(QtCore.Qt.AlignCenter)
        #QtCore에는 정렬이나 이러한 속성값들이 정의되어 있다 
        label1.resize(60,25)

        label2 = QtWidgets.QLabel("라벨2",self)
        label2.setAlignment(QtCore.Qt.AlignRight)
        label2.setStyleSheet("color:red; font-size:20px;")
        #html에서 쓰는 스타일 시트를 그대로 쓸 수가있다
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        


        self.setLayout(layout)
        self.show()

#위의 코드를 실행 시켜주는 코드 
app = QtWidgets.QApplication([])
win = MyWindows()
app.exec_()

