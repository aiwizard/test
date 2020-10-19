# https://iroy123.tistory.com/57

from PyQt5 import QtWidgets

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("이벤트 테스트")
        self.statusBar = self.statusBar()
        self.setMouseTracking(True) #마우스 이벤트를 감시하겠다 true
        self.setGeometry(300,300,400,300)#(x,y,width,heigth)
        self.show()

    #오버라이딩 함수 구현 - 부모에 선언되어 있는 함수를 그대로 써야함으로 함수명을 똑같이 써야한다
    def keyPressEvent(self, e):
        output = "키눌림 <key : {}>".format(e.key())
        self.statusBar.showMessage(output)

    def keyRealeaseEvent(self, e):
        output = "기 띔 <key :{}>".format(e.key())
        self.statusBar.showMessage(output)

    def mouserDoubleClickEvent(self, e):
        button = e.button()
        x = e.x()
        y = e.y()
        gx = e.globalX()
        gy = e.globalY()
        output = "아무스 더블클릭<버튼 :{}, x={}, y={}, gx={}, gy={}>".format(button,x,y,gx,gy)
        self.statusBar.showMessage(output)

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()
        gx = e.globalX()
        gy = e.globalY()
        output = "아무스 이동 < x={}, y={}, gx={}, gy={}>".format(x,y,gx,gy)
        self.statusBar.showMessage(output)

app = QtWidgets.QApplication([])
ex = MyApp()
app.exec_()
