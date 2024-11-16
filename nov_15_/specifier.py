# specifier and modifire 

# class Student:
#     def __init__(self, name, age, city):
#         self.name = name
#         self._age = age
#         self.__city = city
#     def display(self):
#         print(self.name)
#         print(self._age)
#         print(self.__city)
# obj1 = Student("John Doe", 20, "New York")
# obj1.display()

class Student:
    def __init__(self, name, age, city):
        self.name = name
        self._age = age
        self.__city = city
class StudentA(Student):
    def display(self):
        print(self.name)
        print(self._age)
        print(self.__city)
obj = StudentA("John Doe", 20, "New York")
print(obj.name)
print(obj._age)
# print(obj.__city)
# obj.display()
# print(dir(Student))
# print(obj._Student__city)