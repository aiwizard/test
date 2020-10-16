'''
http://pythonstudy.xyz/python/article/121-Tkinter-위젯

이벤트 바인딩 
	위젯.bind(event, handler)
'''

from tkinter import *
root = Tk()
 
def click(event):
    print("클릭위치", event.x, event.y)
    
frame = Frame(root, width=300, height=300)
 
 #왼쪽 마우스 버튼 바인딩
frame.bind("<Button-1>", click) 
 
frame.pack()
root.mainloop()


