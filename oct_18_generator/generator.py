# generator 
# yeild function 
# yeild = generator object hold karta hai 
# return value hold karta hai 
# def gen(n):
#     i=1
#     while i<=n:
#         yield i
#         i=i+1
# n=int(input("enter any num="))
# var = gen(n)
# print(var)
# print(next(var))
# print('hello')
# print('Hi')
# print(next(var))
# print(next(var))
# print(next(var))

# def gen(n):
#     i=1
#     while i<=n:
#         return i
#         i=i+1
# n=int(input("enter any num="))
# var = gen(n)
# print(var)


# def gen(n):
#     i=1
#     while i<=n:
#         print (i)
#         i=i+1
# n=int(input("enter any num="))
# var = gen(n)
# # print(var)

def gen(n):
    i=1
    while i<=n:
        yield i
        i=i+1
n=int(input("enter any num="))
var = gen(n)
print(var)
print(next(var))





