from tkinter import *

root = Tk()
root.title("광재야 놀자~")
root.geometry("640x480")

chkvar = IntVar()
chkbox = Checkbutton(root, text="1", variable=chkvar)
# chkbox.select() # 자동 선택 처리
# chkbox.deselect() # 선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="2", variable=chkvar2)
chkbox2.pack()


def btncmd() :
    print(chkvar.get())
    print(chkvar2.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()