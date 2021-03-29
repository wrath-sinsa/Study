# 표준 입출력 separate, end

# print ("Python", "Java","C++", sep=" vs ", end=" ? ")
# print ("뭐가 더재밌음?")

# import sys
# print ("Python", "Java", file=sys.stdout) #표준 출력
# print ("Python", "Java", file=sys.stderr) #표준 에러

# scores = {"수학" :  0, "영어" :  50, "코딩" :  100}
# for subject, score in scores.items() :
#     # print (subject, score)
#     print (subject.ljust(8), str(score).rjust(4), sep = ":")
# 8칸 공간 확보후 좌정렬        # 4칸 공간 확보후 우정렬

# # 은행 대기 순번
# # 001, 002, 003
# for num in range(1, 21) :
#     print ("대기 번호 : " + str(num).zfill(3)) # zerofill 0채우기

# answer = input("아무 값이나 입력하세요 : ")
# print ("입력하신 값은 " + answer + "입니다")




# 다양한 출력 포맷

# # 빈 자리는 빈 공간, 오른쪽 정렬, 총 10자리 확보
# print ("{0: >10}".format(500)) # :(빈공간)(오른쪽 정렬)(10칸)
# print ("{0:1>10}".format(500)) # :(1)(오른쪽 정렬)(10칸)

# # 양수 +, 음수 -
# print ("{0: >+10}".format(500))
# print ("{0: >+10}".format(-500))

# # 왼쪽 정렬, 빈칸 _
# print ("{0:_<+10}".format(500))

# # 3자리 마다 ,
# print ("{0:,}".format(10000000000000000))

# # 3자리 , +- 부호
# print ("{0:+,}".format(10000000000000000))
# print ("{0:+,}".format(-10000000000000000))

# # 3자리, 부호, 자릿수
# print("{0:^<+30,}".format(10000000000000000))

# ##
# print("{0: >+30,}".format(10000000000000000))
# print("{0:>+30,}".format(10000000000000000))

# # 소수점 출력
# print ("{0:f}".format(5/3))

# # 특정 자리수까지
# print ("{0:.2f}".format(5/3))



# 파일 입출력

# score_file = open("score.txt", "w", encoding="utf8") # encoding은 유니코드 인듯
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close

# score_file = open("score.txt", "r", encoding ="utf8")
# print (score_file.read())
# score_file.close

# score_file = open("score.txt", "r", encoding ="utf8")
# print (score_file.readline()) # 한줄 읽고, 다음 줄로 이동
# print (score_file.readline(), end = "")
# print (score_file.readline())
# print (score_file.readline())
# score_file.close()

# score_file = open("score.txt", "r", encoding ="utf8")
# while True :
#     line = score_file.readline()
#     if not line :
#         break
#     print (line)
# score_file.close()

# score_file = open("score.txt", "r", encoding ="utf8")
# lines = score_file.readlines() # 리스트 형태로 저장
# for line in lines :
#     print (line)
# score_file.close()


# pickle

# import pickle
# profile_file = open("profile.pickle", "wb") # write binory 바이너리?
# profile = {"이름" : "박명수", "나이" : 30, "취미" : ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile 을 profile_file에 저장
# profile_file.close()
 
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)
# print (profile)
# profile_file.close()


# with

# import pickle

# with open("profile.pickle", "rb") as profile_file : 
#     # 파일을 열어서 profile_file 로 저장
#     # with 탈출하면서 알아서 닫힘 (close)
#     print (pickle.load(profile_file))

# with open("study.txt", "w", encoding="utf8") as study_file :
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file : 
#     print (study_file.read())


# Quiz ) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - X 주차 주간 보고 -
# 부서 :
# 이름 : 
# 업무 요약 :

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 : 파일명은 "1주차.txt", "2주차.txt", ... 와 같이 만듭니다.

# for i in range (1, 51) :
#     with open("%d주차.txt"%i, "w", encoding="utf8") as report :
#         report.write("- %d 주차 주간 보고 -"%i)
#         report.write("\n부서 : ")
#         report.write("\n이름 : ")
#         report.write("\n업무 요약 : ")

for i in range (1,51) :
    with open("%d주차.txt"%i,"r",encoding="utf8") as report :
        print(report.read())








