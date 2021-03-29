"""
python = "Python is Amazing"
#print (python.lower())
#print (python.upper())
#print(python[1:6].islower())
#print(len(python))
#print (python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n" , index + 1)
print(index)

print (python.find("Java"))
#find 는 없으면 -1 출력
#print (python.index("Java"))
#index는 오류가 실행되므로 진행 x
print (python.count("n"))
"""
#print ("a" + "b")
#print ("a","b")

# 방법 1
# print ("나는 %d살 입니다." %20)
# print ("나는 %s을 좋아해요" %"파이썬" )
# print ("Apple 은 %c로 시작해요." % "A")

# print ("나는 %s살 입니다." %20)
# print ("나는 %s색과 %s색을 좋아해요." %("파란", "빨간")

# 방법 2
# print ("나는 {}살입니다.".format(20))
# print ("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# print ("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
# print ("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3
# print ("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))
# print ("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))

# 방법 4
# age = int(input("age = "))
# color = input("color = ")
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

# print("백문이 불여일견\n백문이 불여일타")

# \" \' : 무낭 내에 따옴표 출력
# 저는 "나도코딩"입니다.
# print ("저는 "나도코딩"입니다") << 오류 (?)
# print ("저는 \"나도코딩\" 입니다.")
# print ("저는 \'나도코딩\' 입니다.")

# \\ : 문장내에서 \
# print ("C:\\Users\\Nadocoding\\Desktop\\PythonWorkspace>")

# \r : 커서를 맨 앞으로 이동
# print ("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
print ("Redd\bApple")

# \t : 탭
print ("Red \t Apple")