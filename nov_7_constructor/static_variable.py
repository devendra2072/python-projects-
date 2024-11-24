# 9/11/2024
# static variable:-  aisa variable jiski object badlne ke sath value na badle /na change kare static variable hota hai hota hai
# 3 types of method :- instance method ,2 class method , 3 static method 
# static method :- class se koi matlab nahi hota hai , normal method hai
# class Student:
#     school ='SHSS'
#     def __init__(self,name):
#         self.name=name
#         Student.city='bhopal'
#     def new(self):
#         Student.state='M.P'
#     @classmethod
#     def new1(cls):
#         Student.subject='Math'
#         cls.subject2='Hindi'
#     @staticmethod
#     def new2():
#         Student.subject3='physics'     
# obj=Student('devendra')
# obj.new()
# obj.new1()
# obj.new2()
# obj.subject4='sanskrit'
# Student.subject5='english'
# print(Student.city)
# print(Student.school)
# print(obj.name)
# print(Student.subject)
# print(Student.subject2)
# print(Student.subject3)
# print(Student.subject5)
# print(obj.subject4)


# class Student:
#     school ='SHSS'
#     def __init__(self,name):
#         self.name=name
#         Student.city='bhopal'
#     def new(self):
#         Student.state='M.P'
#     @classmethod
#     def new1(cls):
#         Student.subject='Math'
#         cls.subject2='Hindi'
#     @staticmethod
#     def new2():
#         Student.subject3='physics'
#     def display(self):          # yaha 'self' na likhe to static method hai  aur likh dete hai hai instance method hai
#         print(Student.city)
#         print(Student.school)
#         print(obj.name)
#         print(Student.subject)
#         print(Student.subject2)
#         print(Student.subject3)
#         print(Student.subject5)
#         print(obj.subject4)
#         # print(self.name)
# obj=Student('devendra')
# obj.new()
# obj.new1()
# obj.new2()
# obj.subject4='sanskrit'
# Student.subject5='english'
# obj.display()


# callling type 
class Student:
    school ='SHSS'
    def __init__(self,name):
        self.name=name
        Student.city='bhopal'
        print(Student.school)
    def new(self):
        Student.state='M.P'
    @classmethod
    def new1(cls):
        print(Student.city)
        Student.subject='Math'
        cls.subject2='Hindi'
    @staticmethod
    def new2():
        print(Student.school)
        Student.subject3='physics'
    def display(self):
        print(Student.city)
        print(Student.school)
        print(obj.name)
        print(Student.subject)
        print(Student.subject2)
        print(Student.subject3)
        print(Student.subject5)
        print(obj.subject4)
        # print(self.name)
             
obj=Student('devendra')
obj.new()
obj.new1()
obj.new2()
obj.subject4='sanskrit'
Student.subject5='english'

obj.display()