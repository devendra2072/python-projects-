# 08/11/2024
# variable type 
# 1 instance variable 2 static variable 3 local variable
# 1 instance variable ko declear karne ke tarike 2 hai class ke under and class ke bahar 
# carent object  ka current addresh hold karta hai
# inside class instance variable ko declear karna

# 1 instance variable:- aisa variable jiski object badlne ke sath value bhi badal jaye instance variable hota hai
# declearation 
# class Studant:
#     def __init__(self,name):
#         print("hello")
# obj1=Studant('devendra')
# obj2=Studant('abhi')

# class Student:
#     def __init__(self,name):     #inside construtor
#         self.name=name
#     def show(self):             #inside instance method
#         self.age=37
#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
# obj=Student("devendra")
# obj.show()
# obj.display()

# outside class instance variable ko declear karna
# class Student:
#     def __init__(self,name):
#         self.name=name
#     def show(self,age):
#         self.age=age
#     def display(self):
#         print("quli:",self.quli)
#         print("Name:",self.name)
#         print("Age:",self.age)
# obj=Student("devendra")
# obj.show(37)
# obj.quli="b.tech"
# obj.display()

# calling 
# object badlane se value change ho instaanc variable 
# class Student:
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         self.age=37
#     def display(self):
#         print("quli:",self.quli)
#         print("Name:",self.name)
#         print("Age:",self.age)

# obj=Student("devendra")
# obj.show()
# obj.quli="b.tech"
# print(obj.quli)
# print(obj.age)
# print(obj.name)