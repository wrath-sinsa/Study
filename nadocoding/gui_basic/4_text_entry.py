from tkinter import *

root = Tk()
root.title("광재야 놀자~")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)
e.pack()
e.insert(END, "한 줄만 입력하세요")

def btncmd() :
    #갖고오기
    print(txt.get("1.0", END)) # (index1, index2) 1번째줄 0번째 인덱스
    print(e.get())
    #지우기  
    txt.delete("1.0", END)
    e.delete(0, END)


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()