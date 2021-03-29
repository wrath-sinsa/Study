# class Unit : # 부모 클래스
#     def __init__(self, name, hp, speed) : # init는 Unit으로 생성될때 자동으로 들어감
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print ("{} 유닛이 생성되었습니다.".format(name))

#     def move(self, location) :
#         print ("[지상 유닛 이동]")
#         print ("{} : {} 방향으로 이동합니다. [속도 : {}]"\
#             .format(self.name, location, self.speed))

#     def damaged (self, damage) :
#         print ("{} : {} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print ("{} : 현재 체력은 {}입니다.".format(self.name, self.hp))
#         if self.hp <= 0 :
#             print ("{} : 파괴 되었습니다.".format(self.name))


# class AttackUnit(Unit) : # 자식 클래스
#     def __init__(self, name, hp, speed, damage) : # init는 Unit으로 생성될때 자동으로 들어감
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage    

#     def attack(self, location) :
#         print ("{} : {} 방향으로 적군을 공격 합니다. [공격력 : {}]"\
#             .format(self.name, location, self.damage)) # location은 Class 내에 없으므로
#         # 밖에서 가져오고 self.name 같은 경우는 Class 내에서 정의 된 값으로 가져오는 듯

# class Marine(AttackUnit) :
#     def __init__ (self) :
#         AttackUnit.__init__(self, "마린", 40, 1, 5)

#     def stimpack(self) : # 스팀팩 : 일정 시간 이속 공속 증가, 체력 10 감소
#         if self.hp > 10 :
#             self.hp -= 10
#             print ("{} : 스팀팩을 사용합니다. (hp 10 감소)".format(self.name))
#         else :
#             print ("{} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# class Tank(AttackUnit) :
#     seize_developed = False
    
#     def __init__ (self, name, hp, speed, damage) :
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False

#     def set_seize_mode(self) :
#         if Tank.seize_developed == False : 
#             return

#         # 시즈모드 일때 / 아닐때
#         if self.seize_mode == False :
#             print ("{} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage *= 2
#             self.seize_mode = True
#         else :
#             print ("{} : 시즈모드를 해제합니다.".format(self.name))
#             self.damage /= 2
#             self.seize_mode = False
                


# class Flyalbe(Unit) :
#     def __init__(self, name, hp, flying_speed) :
#         self.flying_speed = flying_speed
#         Unit.__init__(self, name, hp, 0) # 0은 지상유닛 이속
    
#     def fly (self, location) :
#         print ("{} : {} 방향으로 날아갑니다. [속도 {}]"\
#             .format(self.name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit, Flyalbe) :
#     def __init__(self, name, hp, flying_speed, damage) : 
#         Flyalbe.__init__(self, name, hp, flying_speed)
#         self.damage = damage
        
#     def move(self, location) :
#         print ("[공중 유닛 이동]")
#         self.fly(location)

# class Wraith(FlyableAttackUnit) :
#     def __init__(self) :
#         FlyableAttackUnit.__init__(self, "레이스", 80, 5, 20)
#         self.clocked = False

#     def clocking(self) :
#         if self.clocked == True :
#             print ("{} : 클로킹 모드 해제합니다".format(self.name))
#             self.clocked = False
#         else :
#             print ("{} : 클로킹 모드 설정합니다".format(self.name))
#             self.clocked = True
        
# def game_start() :
#     print ("[알림] 새로운 게임을 시작합니다.")

# def game_over() :
#     print ("Player : gg")
#     print("[Player] 님이 게임에서 퇴장하셨습니다.")


# # 게임 진행
# game_start()

# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# # t1 = Tank()
# # t2 = Tank()

# w1 = Wraith()

# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# # attack_units.append(t1)
# # attack_units.append(t2)
# attack_units.append(w1)

# for unit in attack_units:
#     unit.move("1시")

# Tank.seize_developed = True
# print ("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# # 마린 스팀팩 탱크 시즈모드 레이스 클로킹
# for unit in attack_units :
#     if isinstance(unit, Marine) :
#         unit.stimpack()
#     elif isinstance(unit, Tank) :
#         unit.set_seize_mode()
#     elif isinstance(unit,Wraith) :
#         unit.clocking()

# for unit in attack_units :
#     unit.attack("1시")

# from random import randint

# for unit in attack_units :
#     unit.damaged(randint(20,21))

# game_over()


# Quiz ) 주어진 코드를 활용하여 부동산 프로그램을 작성.

# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# [코드]
class House :
    # 매물 초기화
    def __init__ (self, location, house_type, deal_type, price, completion_year) :
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self) : 
        print (self.location)
        print (self.house_type)
        print (self.deal_type)
        print (self.price)
        print (self.completion_year)

# class A (House) :
#     def __init__ (self, location, house_type, deal_type, price, completion_year) :
#         House.__init__(self, "강남", "아파트", "매매", "10억", "2010년")

# class B (House) :
#     def __init__ (self, location, house_type, deal_type, price, completion_year) :
#         House.__init__(self, "마포", "오피스텔", "전세", "5억", "2007년")

# class C (House) : 
#     def __init__ (self, location, house_type, deal_type, price, completion_year) :
#         House.__init__(self, "송파", "빌라", "월세", "500/50", "2000년")

houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print ("총 {}대의 매물이 있습니다.".format(len(houses)))
for house in houses :
    house.show_detail()























