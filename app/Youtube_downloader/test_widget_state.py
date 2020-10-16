import tkinter as tk

def switchButtonState():
    if (btn1['state'] == tk.NORMAL):
        btn1['state'] = tk.DISABLED
    else:
        btn1['state'] = tk.NORMAL
    
    if (chkbtn1['state'] == tk.NORMAL):
        chkbtn1['state'] = tk.DISABLED
    else:
        chkbtn1['state'] = tk.NORMAL

app = tk.Tk()
app.geometry("400x100")
btn1 = tk.Button(app, text="Python Button 12345", state=tk.DISABLED)
btn2 = tk.Button(app, text="EN/DISABLE Button 1", command = switchButtonState)
#btn1.pack(side=tk.LEFT)
#btn2.pack(side=tk.RIGHT)
btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)

chkbtn1 = tk.Checkbutton(app, text="Subtitle", state=tk.DISABLE)
#chkbtn1.grid(row=0, column=2)

app.mainloop()
