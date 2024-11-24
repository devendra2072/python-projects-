# positional argument
# def add(x,y):
#     # print(x,y)
#     return x+y
# p=int(input("enter any number = "))
# q=int(input("enter any number = "))
# r=add(p,q)
# print(r)


# # keyword argument
# def add(x,y):
#     # print(x,y)
#     return x+y
# p=int(input("enter any number = "))
# q=int(input("enter any number = "))
# r=add(y=p,x=q)
# print(r)

# default argument

# def add(x=0,y=0):
#     return x+y
# p=int(input("enter any number = "))
# q=int(input("enter any number = "))
# r1=add()
# r2=add(p)
# r3=add(y=q)
# print(r1)
# r4=add(p,q)
# print(r4)

# variable-lenght argument(*args)

# def add(*n):
#     print(n)
#     print(type(n))
#     sum=0
#     for i in n:
#         sum=sum+i
#     print(sum)
# add(10)
# add(10,20,30,30)
# add(10,20,30,40,50)
# print(add(10))


# def add(*n):
#     sum=0
#     for i in n:
#         for i in n:
#             sum=sum+x
#     print(sum)
# x=eval(input("enter any number="))
# print(x)
# print(type(x))
# add(x)
# add((1,2,3,4,5,6))

# keywords variable length argument

# def add(**n):
#     print(n)
#     print(type(n))
#     for i in n.values():
#         print(i)
# add(name='dev', age=37, quli='m.tech')
