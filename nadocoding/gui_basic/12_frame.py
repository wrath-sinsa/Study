import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("광재야 놀자~")
root.geometry("640x480")

Label(root, text="메뉴를 선택하십시오").pack(side="top")

burger_Var = StringVar()
burger = Frame(root, relief="solid", bd=1)
burger.pack(side="left", fill="both", expand=True)
A = Radiobutton(burger, text="햄버거", value="햄버거", variable=burger_Var)
A.pack()
A.select()
Radiobutton(burger, text="치즈버거", value="치즈버거", variable=burger_Var).pack()
Radiobutton(burger, text="찐찌버거", value="찐찌버거", variable=burger_Var).pack()

drink_Var = StringVar()
frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill="both", expand=True)
a = Radiobutton(frame_drink, text="콜라", value="콜라", variable=drink_Var)
a.pack()
a.select()
Radiobutton(frame_drink, text="사이다", value="사이다", variable=drink_Var).pack()

def calling():
    A = burger_Var.get()
    print (A)
    B = drink_Var.get()
    print (B)
    print ("주문 되었습니다.")

Button(root, text="주문", command=calling).pack(side="bottom")





root.mainloop()

# relief는 뭐고 bd는 뭔데!!

