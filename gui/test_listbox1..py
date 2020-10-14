'''
Make Tkinter Listbox Items Always Selected

https://stackoverflow.com/questions/39263298/make-some-tkinter-listbox-items-always-selected
'''

from tkinter import filedialog
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("640x480")

listbox = tk.Listbox(root, exportselection=False, activestyle='none', selectmode=tk.SINGLE)
#for i,item in enumerate(['apples', 'oranges', 'peaches', 'carrots', 'lettuce', 'grapes']):
#  listbox.insert(tk.END, item)
#  if i % 2 == 0:
#    listbox.selection_set(i)
listbox.insert(END, 'apple1')
listbox.insert(END, 'apple2')
listbox.insert(END, 'apple3')
listbox.insert(END, 'apple4')
listbox.insert(END, 'apple5')
listbox.grid(row=6, column=1, sticky='ew')

'''
def always_selected(event):
  widget = event.widget
  for idx in special_items:
      widget.selection_set(idx)

listbox.bind('<<ListboxSelect>>', func=always_selected)
'''


def btncmd_save_as():
  global gfilepath
  gfilepath = filedialog.askdirectory()

def btncmd_check():
  print(listbox.curselection())

btn2 = Button(root, text="저장위치", command=btncmd_save_as)
btn2.grid(row=7, column=1, sticky='ew')

btn3 = Button(root, text="check", command=btncmd_check)
btn3.grid(row=8, column=1, sticky='ew')


root.mainloop()

