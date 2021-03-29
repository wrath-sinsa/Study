# from tkinter import *

# root = Tk()
# root.title("광재야 놀자~")
# root.geometry("640x480")

# menu = Menu(root)

# menu_file = Menu(menu, tearoff= 0)
# menu.add_cascade(label="파일")

# root.config(menu=menu) # 이거 없엇음ㅋ
# root.mainloop()

filename = " 광재 "

with open(filename, "w", encoding="utf8") as file :
    file.write("병신!!")