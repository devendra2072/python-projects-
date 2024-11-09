# constructor in spacial method hai 07/011/2024

# class Student:
#     def __init__(self):
#         print("constructor called")
# obj=Student()

# note : parenthises () ressposible hai is constructor ko call karne ka 
# call nahi hoga 
# class Student:
#     def __init__(self):
#         print("constructor called")
# obj=Student

# constructor ko BAHAR call kar sakte hai  multiple time call kar sakte hai
# class Student:
#     def __init__(self):
#         print("constructor called")
#     def add():
#         print("without constructor called")
# obj=Student()
# # Student.add()
# obj.__init__()
# obj.__init__()
# obj.__init__()

# multiple object se multiple time call kar sakte hai 
# class Student:
#     def __init__(self):
#         print("constructor called")
#     def add():
#         print("without constructor called")
# obj1=Student()
# # Student.add()
# obj2=Student()
# obj3=Student()
# obj4=Student()


# self:= addresh hold karta hai 
# ak class ke under multiple constructor likh sakte hai ya bana sakte hai 
# class Student:
#     def __init__(self):
#         print("constructor called")
        
#     def __init__(self,name):
#         print("name------")
#     def __init__(self,name,age):
#         print("name+age")
#     def __init__(self,name,age,quality):
#         print("name+age+quality")
# obj1=Student("devendra",21,"b.tech")



# class Student:
#     def __init__(self,x):
#         print("constructor called")
        
#     def __init__(self,name):
#         print("name------")
#     def __init__(self,name,age):
#         print("name+age")
#     def __init__(self):
#         print("name+age+quality")
# obj1=Student()


# self and object ka address same hai , and self object ka address hold karta hai , sme bihaviour hota hai
class Student:
    def add(self):            #self
        print("hello")
        print(id (self))
        
obj=Student()
obj.add()
print(id(obj))
