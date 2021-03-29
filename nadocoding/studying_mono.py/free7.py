# 클래스 Class



# # 마린 : 공격 유닛, 군인. 총을 쏨
# name = "마린"
# hp = 40
# damage = 5 

# print ("{} 유닛이 생성 되었습니다.".format(name))
# print ("체력 {}, 공격력 {}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크. 포를 쏨. 일반 모드 / 시즈 모드.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print ("{} 유닛이 생성 되었습니다.".format(tank_name))
# print ("체력 {}, 공격력 {}\n".format(tank_hp, tank_damage))

# def attack(name, location, damage) :
#     print ("{} : {} 방향으로 적군을 공격 합니다. [공격력 {}]".format\
#         (name, location, damage))

# attack (name, "1시", damage)
# attack (tank_name, "1시", tank_damage)

# class Unit :
#     def __init__(self, name, hp, damage) : # init는 Unit으로 생성될때 자동으로 들어감
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print ("{} 유닛이 생성 되었습니다.".format(self.name))
#         print ("체력 {}, 공격력 {}\n".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# __init__


# marine3 = Unit("마린") # 세 변수가 다 필요함.
# marine3 = Unit("마린", 50)

# 멤버 변수


# # 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print ("유닛 이름 : {}, 공격력 : {}".format(wraith1.name,wraith1.damage))

# # 마인드 컨트롤 : 상대방 유닛을 내것으로 만드는 것
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True # 멤버 변수

# if wraith2.clocking == True : # wraith 1 로 바꿀경우 오류
#     print ("{}는 현재 클로킹 상태 입니다".format(wraith2.name))

# method 메소드 attack 과 damaged는 메소드임
# 상속 # 의무병 같은경우 공격력이 없기에 "상속"하여 damage가 있는경우 받음


class Unit : # 부모 클래스
    def __init__(self, name, hp, speed) : # init는 Unit으로 생성될때 자동으로 들어감
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location) :
        print ("[지상 유닛 이동]")
        print ("{} : {} 방향으로 이동합니다. [속도 : {}]"\
            .format(self.name, location, self.speed))


class AttackUnit(Unit) : # 자식 클래스
    def __init__(self, name, hp, speed, damage) : # init는 Unit으로 생성될때 자동으로 들어감
        Unit.__init__(self, name, hp, speed)
        self.damage = damage    

    def attack(self, location) :
        print ("{} : {} 방향으로 적군을 공격 합니다. [공격력 : {}]"\
            .format(self.name, location, self.damage)) # location은 Class 내에 없으므로
        # 밖에서 가져오고 self.name 같은 경우는 Class 내에서 정의 된 값으로 가져오는 듯

    def damaged (self, damage) :
        print ("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print ("{} : 현재 체력은 {}입니다.".format(self.name, self.hp))
        if self.hp <= 0 :
            print ("{} : 파괴 되었습니다.".format(self.name))

# # 메딕 : 의무병!! 이 있기때문에 공격력이 없는 걸 만듦

# # 파이어뱃 : 공격 유닛, 화염방사기.
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)

# 공중유닛

class Flyalbe(Unit) :
    def __init__(self, name, hp, flying_speed) :
        self.flying_speed = flying_speed
        Unit.__init__(self, name, hp, 0) # 0은 지상유닛 이속
    
    def fly (self, location) :
        print ("{} : {} 방향으로 날아갑니다. [속도 {}]"\
            .format(self.name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyalbe) :
    def __init__(self, name, hp, damage, flying_speed) : 
        Flyalbe.__init__(self, name, hp, flying_speed)
        self.damage = damage
        
    def move(self, location) :
        print ("[공중 유닛 이동]")
        self.fly(location)

# # 발키리. 공중 공격 유닛, 한번에 14발 미사일 발사.

# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly("3시")
# valkyrie.attack("3시")

# # 드랍쉽 : 공중 유닛, 수송기. 다양한 유닛들을 수송. 공격 x

# dropship = Flyalbe("드랍쉽", 200, 10)
# dropship.fly("3시")


# 메소드 오버라이딩 method overriding


# # 벌쳐 : 지상 유닛, 기동성 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)


# # 배틀크루저 : 공중 유닛, 체력 완전 좋음, 공격력 좋음
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# # battlecruiser.fly("11시")
# battlecruiser.move("11시")


# pass, super


# 건물
class BuildingUnit(Unit) :
    def __init__(self, name, hp, location) :
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # super는 self 생략 // self().
        self.location = location

# # 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start() :
#     print ("[알림] 새로운 게임을 시작합니다.")

# def game_over() :
#     pass

# game_over()
# game_start()



