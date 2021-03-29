from tkinter import *

root = Tk()
root.title("광재야 놀자~")
root.geometry("640x480")


listbox = Listbox(root, selectmode="extended", height= 0)
# selectmode = single 하나씩 , extended 다중 , height 지정 수만 보여줌
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()



def btncmd() :
    # 삭제
    # listbox.delete(END) # 맨뒤항목 삭제
    # listbox.delete(0) # 맨앞항목 삭제

    # 개수 확인
    print("리스트에는", listbox.size(), "개가 있어요")

    # 항목 확인 (시작 idx, 끝 idx)
    print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))

    # 선택된 항목 확인 (인덱스 위치 반환)
    print ("선택된 항목 :", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()