# create mode open 
# output 
# new1.py
# x
# cp1252
# False
# False
# True
f=open('new1.py','x')
print(f.name)
print(f.mode)
print(f.encoding)
print(f.closed)
print(f.readable())
print(f.writable())