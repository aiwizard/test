import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog

window = Tk()
window.title("Youtube 다운로드")
window.geometry("640x480")

############################################### url 입력
label1 = Label(window, text="URL 입력")
label1.grid(row=0, column=0)

def e_Lclicked(event):
    e.delete(0, END)

def e_Entered(event):
    print("entered")

# 엔트리 - single line
e = Entry(window, width=30)
e.bind("<Button-1>", e_Lclicked)  # WM_LBUTTONCLICK
e.bind("<Return>", e_Entered) # WM_KEYDOWN && ENTER
e.insert(0, "URL")
e.grid(row=0, column=1)

############################################### 저장 폴더 선택 버튼
def btnCmdSelectFolder():
    dir_path = filedialog.askdirectory(parent=window, initialdir="/", title="Please select a folder to save")
    print("dir_path : ", dir_path)

btn_select = Button(window, text="폴더 선택", command=btnCmdSelectFolder)
btn_select.grid(row=1, column=1)

############################################### start 버튼
def error():
    msgbox.showerror("경고", "URL 을 입력하시오")

def btnCmdStart():
    url = e.get()  # 단일라인이므로 범위 지정 필요 없음
    if len(url) == 0:
        error()

btn = Button(window, text="start download", command=btnCmdStart)
btn.grid(row=2, column=1)

###############################################
window.resizable(False, False)
window.mainloop()
