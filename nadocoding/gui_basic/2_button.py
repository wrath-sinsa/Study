from tkinter import *

root = Tk()
root.title("광재야 놀자~")

btn1 = Button(root, text = "버튼1")
btn1.pack()


# 버튼 너비 높이
btn2 = Button(root, padx=5, pady=10, text="버튼2") 
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3333333333333") 
btn3.pack()


#크기 고정
btn4 = Button(root, width=5, height=10, text="버튼4")
btn4.pack()

btn5 = Button(root, width=10, height=5, text="버튼555555555555555")
btn5.pack()

# 색
btn6 = Button(root, fg="red", bg="yellow", text="버튼6")
btn6.pack()

# 불러오기
photo = PhotoImage(file="gui_basic/image.png")
btn7 = Button(root, image=photo)
btn7.pack()

def btncmd() :
    print("버튼 클릭됨")

btn7 = Button(root, text="동작버튼", command=btncmd)
btn7.pack()




root.mainloop()