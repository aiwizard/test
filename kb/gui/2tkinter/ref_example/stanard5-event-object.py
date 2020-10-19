'''
http://pythonstudy.xyz/python/article/121-Tkinter-위젯

이벤트 오브젝트 
'''

from tkinter import *
 
def keyPressed(event):
    # 키보드 문자하나 출력
    print(event.char)
 
root = Tk()
 
frame = Frame(root, width=100, height=100)
# Key 이벤트 바인딩
frame.bind('<Key>', keyPressed) 
frame.place(x=0, y=0)
 
# 키보드 포커를 갖게 한다
frame.focus_set()
 
root.mainloop()


