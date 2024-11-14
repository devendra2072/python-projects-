# 11/11/2024
# loacal variable 
class Student:
    def __init__(self,name):
        self.name = name
    def new1(self):
        global x
        x=20
        print("value of x:", x)
    def new2(self):
        global y 
        print("value of x:", x)
    @classmethod
    def new3(cls):
        y=10
        print("value of y:", y)
    @staticmethod
    def new4():
        z=50
        print(z)
        # print(y)
        print(x)
obj=Student("devendra")
obj.new1()
print(obj.new1())
obj.new2()
obj.new3()
obj.new4()

