'''
pip install pytube3
'''

import tkinter.ttk as ttk   # for Progressbar
import tkinter.messagebox as msgbox  # for msgbox

from tkinter import *
import time  # for progressbar
from tkinter import filedialog

from pytube import YouTube
import os
import subprocess


root = Tk()
root.title("Youtube 다운로드")
#root.geometry("1080x520")
root.geometry("800x600")
root.resizable(False, False)


#----------------------------------------------------- Global variables
#ENTRY1_WIDTH = 111
#LISTBOX_HEIGHT = 10
ENTRY1_WIDTH = 76
LISTBOX_HEIGHT = 14

g_file_size = 0
gfilepath = "./"


# ---------------------------------------------------- 위젯
# 레이블
Label(root, text="Useful contents only", width=12, height=2).grid(row=0, column=1, sticky='ew')
'''
photo1 = PhotoImage(file='../CookPython/gif/dog.gif')
Label(w, image=photo1).grid(row=0, column=1, sticky='ew')
'''

label1 = Label(root, text="Youtube URL: ", width=12, height=2, anchor=E)
label1.grid(row=1, column=0)

label2 = Label(root, text="Path to save: ", width=12, height=2, anchor=E)
label2.grid(row=3, column=0)

label3 = Label(root, text="Title: ", width=12, height=2, anchor=E)
label3.grid(row=4, column=0)


# 엔트리 - single line
e1 = Entry(root, width=ENTRY1_WIDTH, bg='light green')
e1.grid(row=1, column=1)
e1.insert(0, 'https://www.youtube.com/watch?v=OxgiiyLp5pk')

e2 = Entry(root, bg='light green')
e2.grid(row=3, column=1, sticky='ew')
e2.insert(0, "./")

e3 = Entry(root, bg='light yellow')
e3.grid(row=4, column=1, sticky='ew')
e3.insert(0, "You will see the youtube title here.")

# Listbox
listbox = Listbox(root, exportselection=False, selectmode="single", height=LISTBOX_HEIGHT)
listbox.grid(row=2, column=1, columnspan=2, sticky='ew')

# Scrollbar - vertical
sbY = Scrollbar(root, orient="vertical")
sbY.config(command=listbox.yview)
#sbY.pack(side="right", fill="y")
sbY.grid(row=2, column=1, columnspan=2, sticky="nse")
listbox.config(yscrollcommand=sbY.set)

# Scrollbar - horizontal
sbX = Scrollbar(root, orient="horizontal")
sbX.config(command=listbox.xview)
sbX.grid(row=2, column=1, columnspan=2, sticky="ews")
listbox.config(xscrollcommand=sbX.set)


# ProgressBar
p_var2 = DoubleVar()    # 실수형 변수
progressbar = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar.grid(row=5, column=1, columnspan=2, sticky='ew', pady=3)


e4 = Entry(root, bg="light gray")
e4.grid(row=6, column=1, columnspan=2, sticky='ew')
e4.insert(0, "status")


# ---------------------------------------------------- callback
#def on_progress_status(stream = None, chunk = None, file_handle = None, remaining = None):
def on_progress_status(stream, chunk, bytes_remaining):
    progress = (100*(g_file_size-bytes_remaining))/g_file_size
    print(yt.title + "... : {:00.0f}% downloaded".format(progress), end='\r')
    
    # progress
    p_var2.set(progress)       # progress bar 의 값 설정
    progressbar.update()   # GUI 업데이트

    # status
    s = '{}%'.format(int(p_var2.get()))
    e4.delete(0, END)
    e4.insert(0, s)
    

def on_complete(stream, file_path):
    print("Done downloading the video")


# ---------------------------------------------------- 이벤트 핸들러
def btncmd_lookup_format():
    video_url = e1.get()
    if(video_url[:8] != 'https://' or video_url.find('watch?v=') == -1):
        msgbox.showinfo("Error", "적합한 URL 을 입력하시오")
        return

    print(video_url)
    global yt
    yt = YouTube(video_url, on_progress_callback=on_progress_status, on_complete_callback=on_complete)
    '''
    print("[영상 제목]", yt.title)
    print("[영상 게시자]", yt.author)
    print("[조회수]", yt.views)
    print("[평균평점]", yt.rating)
    print("[영상길이(초)]", yt.length)
    print("[연령제한여부]", yt.age_restricted)
    print("[영상 설명]", yt.description)
    print("[썸네일URL]", yt.thumbnail_url)
    '''
    #print("선택된 항목 idx: ", listbox.curselection())
    #print("선택된 항목 값: ", listbox.get(listbox.curselection()))
    #print(len(yt.streams))

    listbox.delete(0, END)  # deleta all

    for i in yt.streams:
        listbox.insert(END, i)

    e3.delete(0, END)
    e3.insert(0, yt.title)

    # Subtitles    
    caption_count = len(yt.captions)
    if(caption_count > 0):
        print("subtitle is downloadable")
        #chkBtnSubtitle['state'] = NORMAL
        #chkBtnSubtitle.set('state') = NORMAL
    else:
        print("There is no subtitles")
        #chkBtnSubtitle['state'] = DISABLED

    for j in yt.captions:
        print(j)


def btncmd_save_as():
    global gfilepath
    gfilepath = filedialog.askdirectory()
    if( len(gfilepath)==0 ):
        gfilepath = './'
    e2.delete(0, END)
    e2.insert(0, gfilepath)


def btncmd_download():
    cursel = listbox.curselection()
    if(cursel == ()):
        msgbox.showinfo("error", "You must choose a media format above first.")
        return

    print(' cursel: {}\n cursel[0]: {}'.format(cursel, cursel[0]))
    id = cursel[0]

    global g_file_size
    g_file_size = yt.streams[id].filesize
    print('gfilepath: ', gfilepath)

    #yt.streams[id].download(output_path=gfilepath, filename = filename, filename_prefix= 'R.I.P_')
    yt.streams[id].download(output_path=gfilepath)

    '''
    # progress
    for i in range(101):    # 0 ~ 100
        time.sleep(0.01)    # 0.01초 대기

        p_var2.set(i)       # progress bar 의 값 설정
        progressbar.update()   # GUI 업데이트

        s = '{}%'.format(int(p_var2.get()))
        e4.delete(0, END)
        e4.insert(0, s)
        '''

    e4.delete(0, END)
    e4.insert(0, "비디오 다운로드 완료. 'mp3 변환 중...'")
    e4.update()

    '''
    if( subtitle.get() != 0 ):
        yt.captions.all()[0]
    '''

    if( mp3.get() == 0 ):
        msgbox.showinfo("알림", "다운로드 완료")
    else:
        print('mp3 conversion start')

        video_filename = yt.streams[id].default_filename
        nameonly = video_filename[:video_filename.rfind('.')]
        audio_filename = nameonly + '.mp3'
        subprocess.call(['ffmpeg', '-i',		#cmd 명령어 수행
            os.path.join(gfilepath, video_filename),
            os.path.join(gfilepath, audio_filename)
        ])
        
        # remove video
        #os.remove(os.path.join(gfilepath, video_filename))


        e4.delete(0, END)
        e4.insert(0, "완료하였습니다")
        e4.update()

        msgbox.showinfo("알림", "다운로드 및 mp3 변환 완료")

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


def e1_clickLeft(event):
  #e1.delete(0, END)
  #e1.select_range(0, 10)
  print('Selection is not implemented yet')
'''
def e2_clickLeft(event):
  e2.delete(0, END)

def e3_clickLeft(event):
  e3.delete(0, END)
'''
e1.bind('<Button-1>', e1_clickLeft)
#e2.bind('<Button-1>', e2_clickLeft)
#e3.bind('<Button-1>', e3_clickLeft)

# ---------------------------------------------------- 버튼
btn = Button(root, text="영상확인", command=btncmd_lookup_format)
btn.grid(row=1, column=2, sticky='ew')

btn2 = Button(root, text="저장위치", command=btncmd_save_as)
btn2.grid(row=3, column=2, sticky='ew')

btn3 = Button(root, text="다운로드", command=btncmd_download)
btn3.grid(row=4, column=2, sticky='ew')
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

'''
def subtitle_check():
    if subtitle.get() == 0:
        print('x')
    else:
        print('y')

def mp3_check():
    if mp3.get() == 0:
        print('xx')
    else:
        print('yy')

command=subtitle_check, 
command=mp3_check, 
'''

mp3 = IntVar()
subtitle = IntVar()  # StringVar() : 문자열, DoubleVar() : 실수형
Checkbutton(root, text="mp3", state=NORMAL, variable=mp3, anchor=W).grid(row=7, column=2, sticky='ew')
chkBtnSubtitle = Checkbutton(root, text="자막", state=DISABLED, variable=subtitle, anchor=W).grid(row=8, column=2, sticky='ew')

###############################################################
root.mainloop()
