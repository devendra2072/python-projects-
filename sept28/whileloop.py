# code repitation in sequence to use in loop
# pep8  py code write karne ke condition

# wap to print 1 to 10 Number

# n=int(input("enter any number="))
# i=1
# while i<=n:
#     # print(i)
#     # print(i,end='')
#    if i<n:  
#     print(i,end=',')
#    else:
#     print(i)
#    i=i+1

# help(print)

# # wap to print even number upto n natural no

# n=int(input("enter any number="))
# i=1
# while i<=n:
#    if n%2==0:   # if given no is even
#        if i%2==0:  #even no
#            if i<n:
#                print(i,end=',')   #output ke liye
#            else:
#                print(i)
#    else:
#        if i%2==0:
#             if i<n-1:
#                print(i,end=",")
#             else:
#                print(i)
#    i=i+1

#  print any even numbers

# n=int(input("enter any number="))
# i=2
# while i<=2*n:
#    if n%2==0:   # if given no is even
#        if i%2==0:  #even no
#            if i<n*2:
#                print(i,end=',')   #output ke liye
#            else:
#                print(i)
#    else:
#        if i%2==0:
#             if i<(n*2)-1:
#                print(i,end=",")
#             else:
#                print(i)
#    i=i+1

#print any odd number

# n=int(input("enter any number="))
# i=1
# while i<=n:
#    if n%2!=0:   # if given no is even
#        if i%2!=0:  #even no
#            if i<n:
#                print(i,end=',')   #output ke liye
#            else:
#                print(i)
#    else:
#        if i%2!=0:
#             if i<n-1:
#                print(i,end=",")
#             else:
#                print(i)
#    i=i+1


#print odd number 
# n=int(input("enter any number="))
# i=1
# while i<=n*2:
#    if n%2!=0:   # if given no is even
#        if i%2!=0:  #even no
#            if i<n*2:
#                print(i,end=',')   #output ke liye
#            else:
#                print(i)
#    else:
#        if i%2!=0:
#             if i<(n*2)-1:
#                print(i,end=",")
#             else:
#                print(i)
#    i=i+1
   
# wap to print sum number
# i=0
# sum=0
# n=int(input("enter any number="))
# while i<=n:
#    sum=sum+i
#    if i<n:  
#     print(i,end=',')
#    else:
#     print(i,end="=")
#    i=i+1
# print(sum,end="")


# wap to print even number upto n natural no

n=int(input("enter any number="))
i=1
sum=0
while i<=n:
   sum=sum+i
   if n%2==0:   # if given no is even
       if i%2==0:  #even no
           if i<n:
               print(i,end='+')   #output ke liye
           else:
               print(i,end="=")
   else:
       if i%2==0:
            if i<n-1:
               print(i,end="+")
            else:
               print(i,end="=")
   i=i+1
print(sum)   
   
   
