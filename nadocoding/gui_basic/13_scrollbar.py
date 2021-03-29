import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("광재야 놀자~")
root.geometry("640x480")


# 프레임 설정
frame = Frame(root)
frame.pack()

# 스크롤
scroll = Scrollbar(frame)
scroll.pack(side="right", fill= "y")

# 리스트박스
listbox = Listbox(frame, selectmode="extended", height = 10, yscrollcommand=scroll.set)
for i in range (1, 32):
    listbox.insert(END, str(i) + "일")
listbox.pack(side ="left")


# 스크롤과 리스트박스 상호작용
scroll.config(command=listbox.yview)

root.mainloop()
