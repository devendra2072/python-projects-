# 14/11/2024  polimorphisma


class Student:
    school = "hssm"  # static variable  ko hi class variable bolte hai 
    def __init__(self, name):  #constructor
        self.name = name  # instance variable
    def new1(self):   # instance method
        Student.city='Bhopal'
        state='M.P.'    #local variable
    @classmethod
    def new2(cls):   # class method
        cls.school_code=101
    @staticmethod         #static method
    def new3():
        print("welcome")
obj = Student('Devendra')
obj.new1()
print(obj.name)
print(Student.city)


# dtl (jango ke liye)