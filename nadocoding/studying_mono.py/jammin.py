"""
from tkinter import *
root = Tk()

lbl = Label(root, text="이름")
lbl.grid(row=0, column=0)

txt = Entry(root)
txt.grid(row=0, column=1)

btn = Button(root, text="OK")
btn.grid(row=0, column=2)

root.mainloop()
"""
"""
from tkinter import *
from tkinter import messagebox

def myClick(event) :
    messagebox.showinfo("마우스", "마우스 오른쪽 버튼이 \
        더블클릭됨")

window = Tk()

window.bind("<Double-Button-3>", myClick)

window.mainloop()
"""
"""
from tkinter import *

window=Tk()

mainMenu = Menu(window)
window.config(menu=mainMenu)
myMenu = Menu(mainMenu)
yourMenu = Menu(mainMenu)
mainMenu.add_cascade(label="나의메뉴",menu=myMenu)
mainMenu.add_cascade(label="나의메뉴",menu=yourMenu)
myMenu.add_command(label="메뉴0")
yourMenu.add_command(label="메뉴1")

window.mainloop()
"""