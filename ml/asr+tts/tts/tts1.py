from tkinter import *

root = Tk()
root.title("Scyan TTS")
#root.iconbitmap("./speaker.ico") 
root.geometry("400x400")


# menu
menubar = Menu(root)

menu_1 = Menu(menubar, tearoff=0)
menu_1.add_command(label="새파일")
menu_1.add_command(label="열기")
menu_1.add_command(label="저장")
menu_1.add_separator()
menu_1.add_command(label="종료")
menubar.add_cascade(label="파일", menu=menu_1)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="파일목록")
helpmenu.add_command(label="정보")
menubar.add_cascade(label="도움말", menu=helpmenu)

root.config(menu=menubar)


# widget
w = Label(root, text="TXT 파일 읽기")
w.grid(row=0, column=0)
e1 = Entry(root)
e1.grid(row=0, column=1)
w = Button(root, text="MP3 생성")
w.grid(row=0, column=2)
w = Button(root, text="▶")
w.grid(row=0, column=3)
w = Button(root, text="■")
w.grid(row=0, column=4)

w = Label(root, text="Phrase 읽기 ")
w.grid(row=1, column=0)
e2 = Entry(root)
e2.grid(row=1, column=1)
w = Button(root, text="구문 저장")
w.grid(row=1, column=2)
w = Button(root, text="구문 읽기")
w.grid(row=1, column=3, columnspan=2, sticky='e')

# frame with Text
frame = Frame(root)
frame.grid(row=2, column=0, columnspan=4, sticky='ew')  
tb = Text(frame, width=50)
tb.pack(side='left', fill='both', expand=True)
scrollbar = Scrollbar(frame)
tb.config(yscrollcommand=scrollbar.set)
scrollbar.config(command= tb.yview)
scrollbar.focus_set()

scrollbar.pack(side='right', fill='y')



mainloop()
