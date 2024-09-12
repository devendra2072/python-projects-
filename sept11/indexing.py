my_str='DEVENDRA'
print(my_str.index('D'))
print(id(my_str.index('D')))
print(type(my_str.index('D')))
print(my_str.index('E'))
x=my_str.index('E')
y=my_str.index('E',(x+1))
print(y)


print(my_str[3])