# super는 다중상속시 맨 앞꺼만 갖구옴

class Unit :
    def __init__(self) :
        print ("Unit 생성자")

class Flyable :
    def __init__(self) :
        print ("Flyable 생성자")

class FlyableUnit(Flyable, Unit) :
    def __init__(self) :
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)
# 드랍쉽
dropship = FlyableUnit() # super 사용시 순서에 
# 따라 Flyable 혹은 Unit 을 갖구옴