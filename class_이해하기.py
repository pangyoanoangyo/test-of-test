from numpy import true_divide


class My_Family:
    def __init__(self, name,age,weight,height):
        self.name = name
        self.nai = age
        self.muge = weight
        self.key = height
        self.bmi = self.key - self.muge
        
        print("나는 {0} 입니다.".format(self.name))
        print("나는 {0} 살이고 몸무게는 {1}kg 입니다.".format(self.nai, self.muge))
        print("아직 {0}살이라 키는 {1}cm이지만 더 클거예요\n".format(self.nai, self.key))
        
    def get_bmi(self):
        return self.bmi
        

My_Family("김유주",10,36,140)


#스타크래프트로 설명합니다.

#마린 : 공격 유닛, 총을 쏜다.

name = "마린" #유닛의 이름
hp = 40 # 유닛의 체력
damage = 5 # 유닛의 공격력

print("{0} 유닛이 생성되었습니다." .format(name))
print("체력은 {0} 공격력은 {1}입니다.\n" .format(hp,damage))

#탱크 : 공격 유닛, 포를 쓴다

tank_name = "탱크" #유닛의 이름
tank_hp = 150 # 유닛의 체력
tank_damage = 35 # 유닛의 공격력

print("{0} 유닛이 생성되었습니다." .format(tank_name))
print("체력은 {0} 공격력은 {1}입니다." .format(tank_hp,tank_damage))


#탱크 : 공격 유닛, 포를 쓴다

tank2_name = "탱크" #유닛의 이름
tank2_hp = 150 # 유닛의 체력
tank2_damage = 35 # 유닛의 공격력

print("{0} 유닛이 생성되었습니다." .format(tank2_name))
print("체력은 {0} 공격력은 {1}입니다." .format(tank2_hp,tank2_damage))


def attack(name,location,damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name,location,damage))
    
attack(name,"1시", damage)
attack(tank_name,"1시", tank_damage)




class Unit:
    def __init__(self,name,hp,damage):
        self.name =name # 멤버변수는 외부에서 사용할수 있음
        self.hp =hp
        self.damage =damage
        print("{0} 유닛이 생성되었습니다." .format(self.name))
        print("체력은 {0} 공격력은 {1}입니다.\n" .format(self.hp,self.damage))
        
marine1 = Unit("마린1", 40, 5)
marine2 = Unit("마린1", 40, 5)
tank1 = Unit("탱크1", 150, 35)
tank2 = Unit("탱크2", 150, 35)


# 레이스 : 공중유니스 비행기입니다.

wraith1 = Unit("레이스", 80, 5)
print("유닛이름 : {0}, 공격력{1}".format(wraith1.name,wraith1.damage))
print("체력은 : {0}으로 빵빵합니다".format(wraith1.hp))


# 마인드 컨트롤 : 상대ㅇ방 유닛을 뱄음

wraith2 = Unit("뺏은 레이스", 80, 5)
wraith2.clocking = True # 밖에서 클래스 함수에 내용을 넣어도 된다.

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))
    
    
    
class AttackUnit:
    def __init__(self,name,hp,damage):
        self.name =name 
        self.hp =hp
        self.damage =damage
    def attack(self,location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name,location,self.damage))
        # 셀프가 들어가면 자기가 사용한걸 사용한는거고 셀프가 없으면 위에 있는걸 사용한다는것
    
    def damaged (self,damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
        self.hp -= damage
        print(" {0} : 현재 체력은 {1} 입니다.".format(self.name,self.hp))
        

#파이어뱃 만들기
firebat1 = AttackUnit("파이어뱃1",50,10) #어택유닛이라는 함수를 통해 생성
firebat1.attack("5시")

#공격을 2번 받는다것을 가정
firebat1.damaged(25) # 데미지드라는 함수를 통해 생성
firebat1.damaged(25)


















