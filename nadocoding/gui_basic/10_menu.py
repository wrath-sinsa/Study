import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("광재야 놀자~")
root.geometry("640x480")

def create_new_file() :
    print("새 파일을 만듭니다.")

def create_new_Window():
    print ("새 윈도우를 엽니다.")

def Open_file():
    print("파일을 엽니다")

menu = Menu(root)

menu_file = Menu(menu, tearoff = 0)

# 메뉴 세부 상황
menu_file.add_command(label="New file", command=create_new_file)
menu_file.add_command(label="New Window", command=create_new_Window)
menu_file.add_separator()
menu_file.add_command(label="Open file", command=Open_file)
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)

## 메뉴 만들기
menu.add_cascade(label="File", menu=menu_file)

## 다른 메뉴 만들기
menu.add_cascade(label="Edit")

## language 메뉴 만들기 (Radio를 통해 택1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="language", menu=menu_lang)

# View 메뉴
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu= menu_view)



root.config(menu=menu) # 필수
root.mainloop()



## tearoff 가 뭔데;;