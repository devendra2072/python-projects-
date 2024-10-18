# function ke under bina code change kiye  function ke behavior change kar deta hai decorator

# decorator
# 1st method 
# def decorator(fun):
#     def inner(x,y):
#         x=x+5
#         y=y+10
#         return fun(x,y)
#     return inner
# def addition(x,y):
#     return (x+y)
# p=int(input("enter 1st num="))
# q=int(input("enter 2nd num="))
# var=decorator(addition)
# x=var(p,q)
# print(x)

# 2nd method 
# def decorator(fun):
#     def inner(x,y):
#         x=x+5
#         y=y+10
#         return fun(x,y)
#     return inner
# @decorator
# def addition(x,y):
#     return (x+y)
# p=int(input("enter 1st num="))
# q=int(input("enter 2nd num="))
# x=addition(p,q)
# print(x)


# multiplay
# def decorator(fun):
#     def inner(x,y):
#         # fun(x,y)
#         return x*y
#     return inner
# @decorator
# def addition(x,y):
#     return (x+y)
# p=int(input("enter 1st num="))
# q=int(input("enter 2nd num="))
# x=addition(p,q)
# print(x)



def decorator(fun):
    def inner(x,y):
        x=x*y
        y=0
        return fun(x,y)
    return inner
@decorator
def addition(x,y):
    return (x+y)

@decorator
def sab(x,y):
    return(x-y)
p=int(input("enter 1st num="))
q=int(input("enter 2nd num="))
x=addition(p,q)
k=sab(p,q)
print(x)
print(k)

