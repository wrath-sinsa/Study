import os
from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480")

menu = Menu(root)

menu_file = Menu(menu, tearoff = 0)

# 파일(F)
filename = "이름 없음"

def open_file():
    if os.path.isfile(filename) : # 파일 있으면 True, 없으면 False
        with open(filename, "r", encoding="utf8") as file :
            txt.delete("1.0", END) # 텍스트 위젯 본문 삭제
            txt.insert(END, file.read())
    else : 
        print ("에러!!!!")
    
def save_file():
    with open(filename, "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END)) # 모든 내용을 가져와서 저장???? 왜? 첫번째줄 0번째...
    print(txt.get("1.0", END))

menu_file.add
menu_file.add_checkbutton(label="새로 만들기(N)")
menu_file.add_command(label="새 창(W)")
menu_file.add_command(label="열기(O)",command=open_file)
menu_file.add_command(label="저장(S)",command=save_file)
menu_file.add_checkbutton(label="다른 이름으로 저장(A)")
menu_file.add_separator()
menu_file.add_checkbutton(label="페이지 설정(U)")
menu_file.add_checkbutton(label="인쇄(P)")
menu_file.add_separator()
menu_file.add_command(label="끝내기(X)",command=root.quit)

menu.add_cascade(label="파일(F)", menu=menu_file)

#편집(E)
menu_edit = Menu(menu, tearoff = 0)

menu_edit.add_checkbutton(label="실행 취소(U)")
menu_edit.add_separator()
menu_edit.add_checkbutton(label="잘라내기(T)")
menu_edit.add_checkbutton(label="복사(C)")
menu_edit.add_checkbutton(label="붙여넣기(P)")
menu_edit.add_checkbutton(label="복사(L)")
menu_edit.add_separator()
menu_edit.add_checkbutton(label="Bing으로 검색(S)")
menu_edit.add_checkbutton(label="찾기(F)")
menu_edit.add_checkbutton(label="다음 찾기(N)")
menu_edit.add_checkbutton(label="이전 찾기(V)")
menu_edit.add_checkbutton(label="바꾸기(R)")
menu_edit.add_checkbutton(label="이동(G)")
menu_edit.add_separator()
menu_edit.add_checkbutton(label="모두 선택(A)")
menu_edit.add_checkbutton(label="시간/날짜(D)")


menu.add_cascade(label="편집(E)", menu=menu_edit)

#서식(O)
menu_format = Menu(menu, tearoff = 0)

menu_format.add_checkbutton(label="자동 줄 바꿈(W)")
menu_format.add_checkbutton(label="글꼴(F)")

menu.add_cascade(label="서식(O)", menu=menu_format)

#보기(V)
menu_view = Menu(menu, tearoff = 0)

menu_view.add_checkbutton(label="확대하기/축소하기")
menu_view.add_checkbutton(label="상태표시줄(S)")

menu.add_cascade(label="보기(V)", menu=menu_view)

#도움말(H)
menu_help = Menu(menu, tearoff = 0)

menu_help.add_checkbutton(label="도움말 보기(H)")
menu_help.add_checkbutton(label="피드백 보내기(F)")
menu_help.add_separator()
menu_help.add_checkbutton(label="메모장 정보(A)")

menu.add_cascade(label="도움말(H)", menu=menu_help)

# 스크롤 바
scroll = Scrollbar(root)
scroll.pack(side="right", fill="y")


# 본문 영역
txt = Text(root, yscrollcommand=scroll.set)
txt.pack(side="left", fill="both", expand=True)

scroll.config(command=txt.yview)


root.config(menu=menu)
root.mainloop()
