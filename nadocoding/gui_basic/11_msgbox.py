import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("광재야 놀자~")
root.geometry("640x480")

def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.") # 메세지 박스 제목, 내용

def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")

def error():
    msgbox.showerror("에러", "에러가 발생 하였습니다.")

def okcancel():
    msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다") # 확인 / 취소를 물음

def retrycancel():
    msgbox.askretrycancel("재시도 / 취소", "일시적 오류입니다. 다시 시도하시겠습니까?") # 다시 시도/ 취소

def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매 하시겠습니까?")

def yesnocancel():
    response = msgbox.askyesnocancel("취소하겠습니까?", message="예매 내역이 저장되지 않았습니다.\
        \n저장후 프로그램을 종료하시겠습니까?")
    # 네 : 저장후 종료
    # 아니오 : 종료
    # 취소 : 계속 작업
    print("응답:", response)
    if response == 1 : # Ture
        print("예")
    elif response == 0 : # False
        print("아니오")
    else : # None  
        print("취소")


Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()

Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()

root.mainloop()


