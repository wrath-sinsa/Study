# 모듈 // 유지 보수 재사용 가능


# import free10_1 as A
# A.price(3)
# A.pice_morning(3)
# A.price_soldier(3)

# form ~ import *의 경우 ~에서 갖고와서 ~.price를 price()로 줄임
# from free10_1 import *
# price(3)
# price_morning(4)
# price_soldier(3)

# # 갖고온 이름을 따로 붙여줌
# from free10_1 import price_soldier as price
# price(10)


# 패키지


# import travel.thailand # travel : 파일, thailand 모듈과 같이 갖고옴
# import. travel.thailand.thailand # 오류

# trip_to = travel.thailand.thailand()
# trip_to.detail()

# from travel.thailand import thailand
# trip_to = thailand()
# trip_to.detail()

# from travel import vietnam as A
# trip_to = A.vietnam()
# trip_to.detail()

# from travel import * # travel 파일에서 모두 갖고 오기? > 오류
# __init__에서 __all__ = ["vietnam"]을 하면 실행됨
# trip_to = vietnam.vietnam()
# trip_to = thailand.thailandP()
# trip_to.detail()

# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(inspect))
# print(inspect.getfile(thailand))


# pip install


# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print (soup.prettify())



# 내장 함수


# input : 사용자 입력 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print ("{}는 아주 좋은 언어입니다!".format(language))

# dir : 객체를 넘겨줬을때 변수와 함수를 표시
# print(dir())
# import random # 외장함수
# # print(dir())
# import pickle
# print(dir())

# print(dir(random))

# lst = [1, 2, 3]
# print(dir(lst))

# name = "Jim"
# print (dir(name))


# 외장 함수


# glob : 경로 내 폴더 / 파일 목록 조회 (윈도우용 dir)
# import glob
# print (glob.glob("*.py")) # 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
# import os

# print(os.getcwd()) #현재 디렉토리

# folder = "sample_dir"

# if os.path.exists(folder) :
#     print("이미 존재하는 폴더")
#     os.rmdir(folder) # remove
#     print(folder, "폴더를 삭제하였습니다.")
# else : 
#     os.makedirs(folder) # 폴더생성
#     print (folder, "폴더를 생성하였습니다.")

# print(os.listdir()) # glob과 비슷하게 씀(?)

# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%M-%D %H:%M:%S"))

# import datetime
# # print("오늘 날짜는", datetime.date.today())

# timedelta : 날짜사이 간격
# today = datetime.date.today() # 오늘 날짜 저장
# td = datetime.timedelta(days = 100)
# print ("우리가 만난지 100일", today + td)


# Quiz) 프로젝트 내에 나만의 시그니처를 남기는 모듈 작성


# 조건 : 모듈 파일명은 byme.py로 작성

# (모듈 사용 예제)
# import byme
# byme.sign()

# (출력 예제)
# 이 프로그램은 나도 코딩에 의해 만들어졌습니다.
# 유튜브 : https://youtube.com
# 이메일 : nadocoding@gmail.com


import byme as A
A.sign()








