# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# # open_account()

# def deposit(balance, money): #입금
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money): #출금
#     if balance >= money:
#         print ("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
#         return balance - money
#     else :
#         print ("출금이 실패되었습니다. 잔액은 {0}원 입니다".format(balance))
#         return balance

# def withdraw_night(balance, money): #저녁 출금
#     commission = 100 # 수수료 100원
#     return commission, balance - money - commission

# balance = 0 # 잔액
# balance = deposit(balance , 1000)
# print (balance)
# balance = withdraw(balance , 2000)
# print (balance)
# balance = withdraw(balance , 500)
# print (balance)
# commission, balance = withdraw_night (balance, 400)
# print ("수수료 {0}원이며, 잔액은 {1} 원입니다.".format(commission, balance))

# def profile(name, age=17, main_lang="Python"):
#     print("이름 : {0}\t나이 : {1} \t언어 : {2}"\
#         .format(name, age, main_lang))

# profile("유재석")

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print ("이름 : {0}\t 나이 : {1}\t".format(name,age), end = " ")
#     print (lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print ("이름 : {0}\t 나이 : {1}\t".format(name,age),\
        end = " ")
    for lang in language:
        print (lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift")