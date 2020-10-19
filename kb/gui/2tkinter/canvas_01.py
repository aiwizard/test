import time
from tkinter import *

window = Tk()

canvas = Canvas(window, width=640, height=480)
canvas.pack()

ball = canvas.create_oval(0,100,50,150, fill='green')

def move_right(event):
  canvas.move(ball, 5, 0)

def move_left(event):
  canvas.move(ball, -5, 0)

def move_up(event):
  canvas.move(ball, 0, -5)

def move_down(event):
  canvas.move(ball, 0, 5)

canvas.bind_all('<KeyPress-Right>', move_right)
canvas.bind_all('<KeyPress-Left>', move_left)
canvas.bind_all('<KeyPress-Up>', move_up)
canvas.bind_all('<KeyPress-Down>', move_down)

window.mainloop()
