# higher order function 
# def my_squr(n):
#     return n**2
# # squre
# my_list=[1,2,3,4,5]
# x=map(my_squr,my_list)
# print(x)
# print(list(x))

# cube
# def my_squr(n):
#     return n**3

# my_list=[1,2,3,4,5]
# x=map(my_squr,my_list)
# print(x)
# print(list(x))



# def my_squr(n):
#     count=0
#     if count>=3 :
#         count=count+1
#         return n+5
#     else:
#         count=count+1
#         return n+10
# my_list=[1,2,3,4,5]
# x=map(my_squr,my_list)
# print(x)
# print(list(x))


# filter=====================
# def my_even(n):
#     if n%2==0 :
#         return n
# my_list=(1,2,3,4,5)
# x=filter(my_even,my_list)
# print(list(x))

# def my_odd(n):
#     if n%2!=0 :
#         return n
# my_list=(1,2,3,4,5)
# x=filter(my_odd,my_list)
# print(list(x))

# def my_odd(n):
#     if n>=3 :
#         return n
# my_list=(1,2,3,4,5)
# x=filter(my_odd,my_list)
# print(list(x))


# def my_odd(n):
#     if n%2==0 :
#         return n
    
# my_list=(1,2,3,4,5)
# x=map(my_odd,my_list)
# print(list(x))





# reduce()====================================
# single o/p
# import functools
# my_list=[1,2,3,5,4]
# def my_max(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# x=functools.reduce(my_max, my_list)
# print(x)

# multiply
# import functools
# my_list=[1,2,3,5,4]
# def my_max(x,y):
#         return x*y
# x=functools.reduce(my_max, my_list)

# print(x)


# 4 lemda function ==================== n input ak sath  le sakta hai 


# n1=int(input("enter number="))
# n2=int(input("enter number="))
# x=lambda x,y: print(x+y)
# x(n1,n2)
# x=lambda x,y:x+y
# print(x(n1,n2))
# x=lambda p,q,r:3*p+4*q+5*r+5 
# print(x(10,20,30)) 


# 1 to 10 number
# n=int(input("enter any number="))
# x=lambda x:[i for i in range(1,x+1)]
# print(x(n))

# even number
# n=int(input("enter any number="))
# x=lambda x:[2*i for i in range(1,x+1)]
# print(x(n))

# odd number
# n=int(input("enter any number="))
# x=lambda x:[(2*i-1) for i in range(1,x+1)]
# print(x(n))

# 10tak even number 
# n=int(input("enter any number="))
# x=lambda x:[i for i in range(1,x+1) if i%2==0]
# print(x(n))

# 10 tak odd number
# n=int(input("enter any number="))
# x=lambda x:[i for i in range(1,x+1) if i%2!=0]
# print(x(n))

# even or odd       
# n=int(input("enter any number="))
# x=lambda x:["even" if x%2==0 else "odd"]
# print(x(n))


# my_list = [1,2,3,4,5]
# print(list(map(lambda x: x**2, my_list)))

# print(list(map(lambda x:"even" if x%2==0 else "odd",my_list)))