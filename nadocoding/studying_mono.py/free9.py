# 예외 처리


# try :
#     print ("나누기 전용 계산기")
#     nums = []
#     nums.append(int(input("1숫자 입력 : ")))
#     nums.append(int(input("2숫자 입력 : ")))
#     # nums.append(int(nums[0] / nums[1]))
#     print ("{} / {} = {}".format(nums[0],nums[1],nums[2]))
# except ValueError:
#     print ("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err :
#     print (err)
# except Exception as err:
#     print ("알 수 없는 에러 발생")
#     print(err)


# 에러 발생시키기
# 사용자 정의 예외 처리
# finally



# class BigNumberError(Exception) : 
#     def __init__(self, msg) :
#         self.msg = msg

#     def __str__(self) :
#         return self.msg

# try :
#     print ("한자리 나눗셈 계산기")
#     num1 = int(input("1숫자 입력 : "))
#     num2 = int(input("2숫자 입력 : "))
#     if num1 >= 10 or num2 >= 10 :
#         raise BigNumberError("입력값 : {}, {}".format(num1, num2))
#     print("{} / {} = {}".format(num1, num2, int(num1 / num2)))
# except ValueError :
#     print ("잘못된 값 입력함. 한자리만 입력하셈")
# except BigNumberError as err:
#     print ("에러 발생. 한자리 숫자만 입력하셈")
#     print (err)
# finally :
#     print ("계산기를 이용해 주셔서 감사합니다.")



# Quiz) 동네에 항상 대기 손님 있는 치킨집.
# 자동 주문 시스템 제작함.
# 예외 처리 구문 넣으셈.

# 조건 1 : 1보다 작거나 숫자가 아닐경우 ValueError 로 처리
#         출력 메시지 : "잘못된 값을 입력함"

# 조건2 : 총 치킨량은 10 마리
#         치킨 소진시 사용자 정의 에러 [SoldOutError]를 발생시키고 프로그램 종료
#         출력 메시지 : "재고가 소진되어 더이상 주문 받지 않음"

# [코드]

chicken = 10
waiting = 1
class SoldOutError(Exception) :
    pass

while (True) :
    try :
        print ("[남은 치킨 : {}]".format(chicken))
        order = int(input("몇 마리 주문 하겠습니까? : "))
        if order > chicken :
            print ("재료가 부족합니다.")
            print ("{} 마리 이하만 주문 가능합니다".format(chicken))
        elif order < 1 :
            raise ValueError    
        else : 
            print ("[대기번호 {}] {}마리 주문 함".format(waiting, order))
            waiting += 1
            chicken -= order
        if chicken == 0 :
            raise SoldOutError
    except ValueError :
        print ("잘못된 값을 입력하셨습니다.")
    except SoldOutError :
        print ("재고가 소진되어 주문받지 않습니다")
        break






































