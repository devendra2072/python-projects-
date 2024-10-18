# eval run time pe data type pahchan leta hai 
# methometical calculation karvane ke liye 
# collection=eval(input("enter any number="))
# print(collection)
# print(type(collection))

#  o/t:-enter any number="dev" 
# 3
# collection=eval(input("enter any number="))
# print(collection)
# print(type(collection))
# count=0
# for i in collection:
#     count=count+1
# print(count)


def my_len(collection):
    count=0
    for i in collection:
        count=count+1
    return count
var_call=eval(input("enter any collection="))
my_len=my_len(var_call)
print("len=",my_len)