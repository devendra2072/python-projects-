# ==================armstrong=================
# n=int(input("enter any number ="))
# m=x=n
# sum=0
# digit=0
# i=0
# while i<n:
#     n=n//10
#     digit=digit+1
# print(digit)
# while i<m:
#     last_digit=m%10
#     sum=sum+last_digit**digit
#     m=m//10
# if x==sum:
#     print("it is armstrong")
# else:
#     print("it is not armstrong")

# ====================================pelindrom==============

# n=input("enter any value=")
# x=n[::-1]
# if n==x:
#     print("given value is pelindrom")
# else:
#     print("given value is not pelindrom")

# =================second method
# ===========================reverse order====================
# n=int(input("enter any value="))
# digit=0
# i=0
# while i<n:
#     reverse=n%10
#     digit=digit*10+reverse
#     n=n//10
# print("reverse digit =",digit)

# wap to the pelindrom or not pelindrom
# n=input("enter any value=")
# x=""  
# for i in n:
#     x=i+x
# if n==x:
#     print("given value is pelindrom")
# else:
#     print("given value is not pelindrom")

# ============= febonicci============= 
'''n=int(input("enter any value="))
a=0
b=1
i=1
print(a,end=',')
print(b,end=',')
while i<=(n-2):
    c=a+b
    a=b
    b=c
    if i<n-2:
        print(c,end=' ')
    else:
        print(c)
    i=i+1'''
    