def sangfeel():
    print("그는 열심히 노력중입니다")

def sadyou():
    for i in range(1,10):
        print("당신은 {0}번 차였습니다".format(i))

def wtf(a,b,c):
    
    c = a + b
    print(c)


print(sangfeel())

    

# def for_you():
#     for i in range(0,11):
#         if i > 0 :
#             print("{0}입니다".format(i))
#         else :
#             i == 10
#             print("끝")
        
# for_you()
        

# a= 10
# while a < 11:
#     a = a -1
#     if a > 0 :
#         print("이제 {0}발 남았다".format(a))
#     else :
#         a == 1
#         print("이제 죽어랏!")
#         break
        

# print(a)
        
    

class present:
    def __init__(self,apple,orange,berry):
        self.apple = apple
        self.orange = orange
        self.berry =berry
    
    # def gift_set(self,apple,orange,berry):
    #     print("이것은{0},저것은{1},그리고{2}".fotmat(apple,orange,berry))
        

gift = present()
gift.apple=10
gift.orange=20
gift.berry=30

print(gift(1,2,3))
    