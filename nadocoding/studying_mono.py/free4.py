# 사전
"""
a = {3:"유재석", 100:"김태호"}

# print (a[3],a[100])
print (a.get(3))
# print (a.get(5))

# get 은 없을 때 None 출력
print (a.get(5))
# 얘는 없으면 오류
print (a[5])
"""
"""
# a = {3:"유재석", 100:"김태호"}

a = { "A-3" : "유재석", "B-100" : "김태호" }
print (a["A-3"])

# 새 손님
print (a)
a["A-3"] = "김종국"
a["C-20"] = "조세호"
print (a)

# 간 손님
del a["A-3"]
print (a)

# key 들만 출력
print (a.keys())

# value 들만 출력
print (a.values())

# key, value 쌍으로 출력
print (a.items())

# 폐점
a.clear()
print (a)
"""
# 튜플
"""
menu = ("돈까스", "치즈까스")
print (menu)

# menu.add("생선까스")

name = "김종국"
age = 20
hobby = "코딩"
print (name, age, hobby)

abc = b = (name, age, hobby) = ("김종국", 20, "코딩")
print (abc)
"""
# 집합 (set)
# 중복 x 순서 x
"""
my_set = {1,2,3,3,3}
print (my_set)
java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합
print (java & python)
print (java.intersection(python))

# 합집합 
print ( java | python )
print (java.union(python))

# 차집합
print (java - python)
print (java.difference(python))

# python 추가
python.add("김태호")
print (python)

# python 제거
java.remove("김태호")
print (java)
"""
# 자료 구조 변경
"""
menu = {"커피", "우유", "주스"}
print (menu, type(menu))

menu = list(menu)
print (menu, type(menu))

menu = tuple(menu)
print (menu, type(menu))

menu = set(menu)
print (menu, type(menu))

a = {0 : 1 , 1 : 0}
print (a, type(a))
a = set(a)
print (a, type(a))
a = dict (a)
print (a, type(a))
"""

"""
Quiz) 추첨 프로그램 작성

조건 1 : 댓글 20개 아이디 1~20
조건 2 : 무작위 추첨 중복 x
조건 3 : random 모듈 shuffle 과 sample 이용

출력 예제

*** 당첨자 발표 ***
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
*** 축하합니다 ***

활용 예제
from random import *
lst = [1, 2, 3, 4, 5]
print (lst)
shuffle(lst)
print (lst)
print (sample(lst, 1))
"""

from random import *
"""
lst = []
N = int(input("N = "))
for i in range (N) :
    lst.append(i)
"""
lst = list(range(1, 21))
shuffle(lst)
"""
a = sample(lst, 1)
lst = list (set(lst) - set(a))
b = sample(lst, 3)
"""
a = sample(lst, 4)

print ("*** 당첨자 발표 ***")
print ("치킨 당첨자 : {0}".format(a[0]) )
print ("커피 당첨자 : {0}".format(a[1:4]) )
print ("*** 축하드립니다 ***")