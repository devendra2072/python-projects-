#  wap to print the sum of print number
# sum=0
# n=int(input("enter no = "))
# for i in range(1,n+1):
#     sum=sum+i
#     if i<n:
#         print(i,end="+")
#     else:
#         print(i,end="=")
# print(sum)

# wap to print of sum of even number upto n natural number
# sum=0
# n=int(input("enter any number="))
# for i in range(2,n+1,2):
#    sum=sum+i
#    if i<n:   # if given no is even
#        print(i,end="+")
#    else :
#        print (i,end="=")  
# print(sum)

# wap to print the of sum of n even numbers
# sum=0
# n=int(input("enter any nubmer="))
# for i in range(1,n+1):
#     sum=sum+2*i
#     if i<n:
#         print(2*i,end=",")
#     else:
#         print(2*i,end="=")
# print(sum)



# wap to print the sum of n odd numbers

# sum=0
# n=int(input("enter any nubmer="))
# for i in range(1,n+1):
#     sum=sum+(2*i-1)
#     if i<n:
#         print((2*i-1),end=",")
#     else:
#         print((2*i-1),end="=")
# print(sum)



# number = int(input("Enter a number = "))

# # Print the multiplication table using a for loop
# print(f"Multiplication Table for {number}:")
# for i in range(1, 11):  # Loop from 1 to 10
#     result = number * i
#     # print(f"{number} x {i} = {result}")
#     print(result)

# anagram using python=======

a = "devendra"
b = "vendrad"
p = [a[i] for i in range(0,len(a))]
p.sort()
r = [b[i] for i in range(0,len(b))]
r.sort()
if p==r:
    print("this is anagram")
else:
    print("not anagram")
