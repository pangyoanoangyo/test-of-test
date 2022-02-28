class MyClass:
    def __init__(self,name,num,bundan,dangbun):
        self.n = name
        self.num = num
        self.b = bundan
        self.d = dangbun
        print("제 이름은 {0}이고, 저는 {1}번이며, {2}분단, {3}당번 입니다.".format(self.n,self.num,self.b,self.d))
        

MyClass("김상필",18,4,"청소")




