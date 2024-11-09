# import module ko call karne ke liye  ya bulane ke liye use karte hai 

# import my_module
# p=int(input("Enter 1st num="))
# q=int(input("Enter 2st num="))
# z1=my_module.add(p,q)
# z2=my_module.sub(p,q)
# print(z1,z2)

# from ka use module ko light weight bhi banate hai sath main call bhi karte hai
# (* ) ka use all ke liye hota  hai 
# from my_module import add ,sub,x,y
# print(x,y)
# z1=add(x,y)
# z2=sub(x,y)
# print(z1,z2)

from my_module import *
print(x,y)
z1=add(x,y)
z2=sub(x,y)
z3=multi(x,y)
z4=div(x,y)
print(z1,z2,z3,z4)



# .py file is called module 
# collection of .py .py ....... file is called librery
# in filo main __init__.py   add ho jaye to ye package hota hai..............