## 리스트에 있는 M번째 리스트 N 번째 원소를 1로 바꿈
def Book (lst) :
    M = int(input("열 입력 : "))
    N = int(input("행 입력 : "))
    lst[M-1][N-1] = 1
    count = 1
    print ("%d행 %d열 예약 되었습니다."%(M,N))
    return (lst, count)
##

## 리스트에 있는 M번째 리스트 N 번째 원소를 0로 바꿈
## count 는 좌석 개수
def Cbook (lst) :
    M = int(input("열 입력 : "))
    N = int(input("행 입력 : "))
    lst[M-1][N-1] = 0
    count = 1
    print ("%d행 %d열 예약 취소되었습니다."%(M,N))
    return (lst, count)

## 실행
def Print (A) : 
    print ("상영관 1: 잔여 좌석 %d / 80"%a)
    print (end = "    ")
    for i in range (1, 11) :
        print (i, end = " ")
    print ("")
    for i in range (30) :
        print ("=", end = "")
    print ("")
    for i in range (8) :
        print ("%d : "%(i+1), end ="")
        for j in range (10) :
            print (lst[i][j], end = " ")
        print ("")

## 2 차원 리스트 만듦
lst = []
for i in range (8) :
    lst2 = []
    for j in range (10) :
        lst2.append(0)
    lst.append(lst2)
##

## 좌석 개수
a = 0
##

## 메뉴
m = 0
while m != 4 :
    print ("1. 예약하기")
    print ("2. 예약 취소하기")
    print ("3. 좌석 출력하기")
    print ("4. 종료")
    m = int(input("메뉴 선택 (종료시 4) : "))
    if m == 1 :
        A = Book(lst)
        a += A[1]
        lst = A[0]
        print ("")
    elif m == 2 :
        B = Cbook(lst)
        a -= B[1]
        lst = B[0]
        print ("")
    elif m == 3 : 
        Print(lst)
        print ("")
    else : 
        if m != 4 :
            print ("메뉴 선택 오류")
        print ("종료")
##


