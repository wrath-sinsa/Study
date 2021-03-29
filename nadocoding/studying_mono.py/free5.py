# if

# weather = input("오늘 날씨는 어때요? : ")
# while weather != "몰라요" :
#     if weather == "비" :
#         print("우산 챙겨")
#     elif weather == "미세먼지" :
#         print("마스크 써")
#     elif weather == "맑음" :
#         print("준비물 필요없음")
#     else :
#         print("나도 몰라")
#     weather = input("오늘 날씨는 어때요? : ")

# for

# for waiting_no in [0, 1, 2, 3, 4, 5] :
#     print ("대기번호 : %d"%waiting_no)
# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks :
#     print ("%s, 커피가 준비 되었습니다."%customer)

# while

# while True :
#     print (1)

# continue 와 break

# absent = [2, 5] 
# no_book = [7]
# for student in range (1,11) :
#     if student in absent :
#         continue
#     elif student in no_book :
#         print ("%d는 교무실로 따라와!"%student)
#         break
#     print ("%d, 책 읽어"%student)

# 한줄 for 문

# students = [1, 2, 3, 4, 5]
# print (students)
# students = [i+100 for i in students]
# print (students)

# students = ["Iron man", "Thor", "I am groot"]
# print (students)
# # students = [len(i) for i in students]
# # print (students)
# students = [i.upper() for i in students]
# print (students)

# 퀴즈 5

# Quiz) 당신은 택시 기사입니다.
# 50명 승객

# 조건 1 : 승객 별 운행 소요시간은 5분 ~ 50분 사이의 난수
# 조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2분

# from random import randint

# cnt = 0
# for i in range (50) :
#     tm = randint(5,50)
#     if 5 <= tm <= 15 :
#         print ("[O] %d번째 손님 (소요시간 : %d)"%(i+1, tm))
#         cnt += 1
#     else :
#         print ("[ ] %d번째 손님 (소요시간 : %d)"%(i+1, tm))
# print ("총 탑승 승객 : %d" %cnt)

# 퀴즈 6

# Quiz ) 표준 체중 구하기

# 표준 체중 : 각 개인 키에 맞는 체중

# 남자 : 키^2(m) x 22
# 여자 : 키^2(m) x 21

# 조건1 : 표준 체중 함수 내에서 계산
#     * 함수명 : std_weight
#     * 전달값 : 키(height), 성별(gender)
# 조건2 : 표준체중은 소수점 둘째자리까지 표시

# (예제)
# 키 175cm 남자 표준 체중은 67.38kg 입니다.

# def std_weight (height, gender) :
#     height2 = float(height / 100)
#     if gender == 0 : # 남
#         std_weight = height2 * height2 * 22
#         print ("키 %dcm 남자 표준 체중은 %.2f 입니다"%(height, std_weight))
#     else : # 녀
#         std_weight = height2 * height2 * 21
#         print ("키 %dcm 여자 표준 체중은 %.2f 입니다"%(height, std_weight))

# from random import randint

# for i in range (20) :
#     gender = randint(0,1)
#     height = randint(150,190)
#     std_weight (height, gender)

