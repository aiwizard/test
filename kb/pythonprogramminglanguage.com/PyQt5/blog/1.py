# https://iroy123.tistory.com/57

from PyQt5 import QtWidgets #QtWidgets이녀석 이름 떄문에 에러가 생겼따 이름 대소문자 구분 꼭 
import sys

#보통 이 PyQt5를 사용하는 방법 
class MyWindows(QtWidgets.QWidget):
    def __init__(self): #생성자를 만들어 줘야한다 
        super().__init__() #부모의 생성자 호출 
        self.setWindowTitle("파이썬 지유아이")
        self.resize(400,300)
        self.show()

app = QtWidgets.QApplication([])
win = MyWindows()
sys.exit(app.exec_()) # 윈도우가 닫힐떄 시스템이 끝날수 있도록 

'''
#이렇게 쓰기도 한다 
app = QtWidgets.QApplication([])
win = QtWidgets.QDialog()
win.setWindowTitle("파이썬 다이얼로그")
win.show()
app.exec_()
'''

