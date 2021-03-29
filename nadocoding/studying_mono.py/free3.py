"""
# Quiz) 변수를 이용하여 다음 문장을 출력
station = input("장소 : ")
print("%s행 열차가 들어오고 있습니다."%station)
"""

"""
# Quiz) 코딩 스터디모임

# 조건 1 : 랜덤 날짜
# 조건 2 : 월별 날짜 최소값인 28 이내로 함
# 조건 3 : 1~3일은 스터디 준비를 해야 하므로 제외.

# 예제 : 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.

from random import randint

a = randint(4,28)
print ("오프라인 스터디 모임 날짜는 매월 ",str(a),"일로 선정되었습니다")
"""

"""
# Quiz) 사이트별로 비밀번호를 만들어주는 프로그램.

# 예) https://naver.com
# 규칙 1 : https:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 . 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 "e" 갯수 + "!"로 구성
#                         nav         5               1          ! 
# 예) 생성된 비밀번호 : nav51!

# url = "https://naver.com"
url = "https://youtube.com"
my_str = url.replace("https://", "") # 규칙 1
my_str = my_str[:my_str.index(".")] # 규칙 2 ## . 을 찾아서 그전까지
password = my_str[0:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print ("{0}의 비밀번호는 {1}입니다.".format(url, password))
"""


