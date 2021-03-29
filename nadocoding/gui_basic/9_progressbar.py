import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("광재야 놀자~")
root.geometry("640x480")

p_var = DoubleVar()
progressbar = ttk.Progressbar(root, maximum=100, length=150, mode="determinate", variable= p_var)
progressbar.pack()



def btncmd() :
    for i in range (101) :
        time.sleep(0.1)

        p_var.set(i)
        progressbar.update()
        print(p_var.get())



btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()