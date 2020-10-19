import tkinter.ttk as ttk   # for Progressbar
import tkinter.messagebox as msgbox  # for msgbox
from tkinter import *
import time  # for progressbar
from tkinter import filedialog


root = Tk()
root.title("Youtube 다운로드")
root.geometry("640x480")


# ---------------------------------------------------- 위젯
# 레이블
label1 = Label(root, text="URL to download: ", width=16, height=2)
label1.grid(row=0, column=0)

label2 = Label(root, text="Path to save: ", width=16, height=2)
label2.grid(row=2, column=0)

label3 = Label(root, text="File name: ", width=16, height=2)
label3.grid(row=3, column=0)

# 엔트리 - single line
e1 = Entry(root, width=50, bg='light blue')
e1.grid(row=0, column=1)
e1.insert(0, "youtube url")

e2 = Entry(root)
e2.grid(row=2, column=1, sticky=E+W)
e2.insert(0, "download path here")

e3 = Entry(root)
e3.grid(row=3, column=1, sticky=E+W)
e3.insert(0, "filename")

listbox = Listbox(root, selectmode="single", height=10)
listbox.grid(row=1, column=1, columnspan=2, sticky=E+W)

# ProgressBar
p_var2 = DoubleVar()    # 실수형 변수
progressbar = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar.grid(row=4, column=1, columnspan=2, sticky=E+W, pady=3)

e4 = Entry(root, bg="light gray")
e4.grid(row=5, column=1, sticky=E+W)
e4.insert(0, "%")


# ---------------------------------------------------- 이벤트 핸들러
def btncmd_lookup_format():
    print(e1.get())  # 단일라인이므로 범위 지정 필요 없음

    #print("선택된 항목 idx: ", listbox.curselection())
    #print("선택된 항목 값: ", listbox.get(listbox.curselection()))

    listbox.delete(0, END)  # deleta all

    listbox.insert(0, "1사과")
    listbox.insert(1, "2딸기")
    listbox.insert(2, "3바나나")
    listbox.insert(END, "4수박")
    listbox.insert(END, "5수박")
    listbox.insert(END, "6수박")
    listbox.insert(END, "7수박")
    listbox.insert(END, "8수박")
    listbox.insert(END, "9수박")
    listbox.insert(END, "10수박")
    listbox.insert(END, "11수박")
    listbox.insert(END, e1.get())

    e3.delete(0, END)
    e3.insert(0, 'yt.title')


def btncmd_save_as():
    filename = filedialog.askdirectory()
    e2.delete(0, END)
    e2.insert(0, filename)


def btncmd_download():
    for i in range(101):    # 0 ~ 100
        time.sleep(0.01)    # 0.01초 대기

        p_var2.set(i)       # progress bar 의 값 설정
        progressbar.update()   # GUI 업데이트

        s = '{}%'.format(int(p_var2.get()))
        e4.delete(0, END)
        e4.insert(0, s)
        
'''
def info():
    msgbox.showinfo("알림", "정상적으로 완료되었습니다")

def okcancel():
    ret = msgbox.askokcancel("확인 / 취소", "예매 하실래요?")
    if ret == 1:
        print("ok")
    elif ret == 0:
        print("cancel")

#def btncmdImage():
#    msgbox.showinfo("이미지버튼", "이미지도 되네")
'''

# ---------------------------------------------------- 버튼
btn = Button(root, text="가져오기", command=btncmd_lookup_format)
btn.grid(row=0, column=2, sticky=E+W)

btn2 = Button(root, text="저장위치", command=btncmd_save_as)
btn2.grid(row=2, column=2, sticky=E+W)

btn3 = Button(root, text="다운로드", command=btncmd_download)
btn3.grid(row=3, column=2, sticky=E+W)
'''
Button(root, command=info, text="알림").pack()
Button(root, command=okcancel, text="확인 취소").pack()

btnProgress = Button(root, text="진행상황", command=btncmdProgress)
btnProgress.pack()
'''
'''
photo = PhotoImage(
    file="D:/work/in progress/학습 - 조각 학습 대상/python/gui_basic/img.png")
btnImage = Button(root, image=photo, text="버튼6", command=btncmdImage)
btnImage.pack()
'''

###############################################################
root.mainloop()
