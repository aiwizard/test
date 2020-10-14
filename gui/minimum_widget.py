import tkinter.ttk as ttk   # for Progressbar
import tkinter.messagebox as msgbox  # for msgbox
from tkinter import *
import time  # for progressbar

root = Tk()
root.title("Youtube 다운로드")
root.geometry("640x480")


# ---------------------------------------------------- 위젯
# 레이블
label1 = Label(root, text="안녕하세요")
label1.pack()

# 텍스트 - multiple line
txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "Text: 여러 라인으로 글자를 입력 가능해요")

# 엔트리 - single line
e = Entry(root, width=30)
e.pack()
e.insert(0, "Entry: 한 줄만 입력 가능")

# 리스트박스
listbox = Listbox(root, selectmode="single", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

# ProgressBar
p_var2 = DoubleVar()    # 실수형 변수
progressbar = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar.pack()


# ---------------------------------------------------- 이벤트 핸들러
def btncmd():
    # 내용 출력
    # 멀티라인 이므로 범위 지정 (1: 첫번째 라인, 0: 0번째 컬럼, END: 끝 까지)
    print(txt.get("1.0", END))
    print(e.get())  # 단일라인이므로 범위 지정 필요 없음

    print("리스트 갯수: ", listbox.size())
    print("1번 째 부터 3번째 항목: ", listbox.get(0, 2))     # 항목 확인 (시작 idx, 끝 idx)
    print("선택된 항목 idx: ", listbox.curselection())
    print("선택된 항목 값: ", listbox.get(listbox.curselection()))


def btncmd2():
    # 각 위젯의 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

    # listbox.delete(END) # 맨 마지막 항목 삭제
    # listbox.delete(0)   # 첫 항목 삭제
    listbox.delete(listbox.curselection())


def info():
    msgbox.showinfo("알림", "정상적으로 완료되었습니다")


def okcancel():
    ret = msgbox.askokcancel("확인 / 취소", "예매 하실래요?")
    if ret == 1:
        print("ok")
    elif ret == 0:
        print("cancel")


def btncmdProgress():
    for i in range(101):    # 0 ~ 100
        time.sleep(0.01)    # 0.01초 대기

        p_var2.set(i)       # progress bar 의 값 설정
        progressbar.update()   # GUI 업데이트
        print("진행상황: ", p_var2.get())


def btncmdImage():
    msgbox.showinfo("이미지버튼", "이미지도 되네")


# ---------------------------------------------------- 버튼
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

btn2 = Button(root, text="지우기", command=btncmd2)
btn2.pack()

Button(root, command=info, text="알림").pack()
Button(root, command=okcancel, text="확인 취소").pack()

btnProgress = Button(root, text="진행상황", command=btncmdProgress)
btnProgress.pack()

photo = PhotoImage(
    file="D:/work/in progress/학습 - 조각 학습 대상/python/gui_basic/img.png")
btnImage = Button(root, image=photo, text="버튼6", command=btncmdImage)
btnImage.pack()

###############################################################
root.mainloop()

'''
# pack 대신 grid 로 배치를 맘대로
    btn = Button(root, text="입력", width=5, height=2)          # width, height
    btn.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)   # sticky: 지정한 방향으로 늘려라
'''
