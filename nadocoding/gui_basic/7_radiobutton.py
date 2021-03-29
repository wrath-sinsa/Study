from tkinter import *

root = Tk()
root.title("광재야 놀자~")
root.geometry("640x480")

Label(root, text="버거").pack()
burger_var = StringVar()
btn_burger1 = Radiobutton(root, text="햄버거", value="햄버거", variable = burger_var)
btn_burger2 = Radiobutton(root, text="치즈버거", value="치즈버거", variable = burger_var)
btn_burger3 = Radiobutton(root, text="치킨버거", value="치킨버거", variable = burger_var)

btn_burger1.pack()
btn_burger1.select()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="음료").pack()
drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable = drink_var)
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable = drink_var)
btn_drink3 = Radiobutton(root, text="환타", value="환타", variable = drink_var)

btn_drink1.pack()
btn_drink1.select()
btn_drink2.pack()
btn_drink3.pack()


def btncmd() :
    print(burger_var.get())
    print(drink_var.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()