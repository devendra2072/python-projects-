# in-built-function--------------

# my_dict={'x':10,'y':20,'z':30}
# print(my_dict)
# print(len(my_dict))
# print(max(my_dict))
# print(min(my_dict))
# print(dict(my_dict))
# print(id(my_dict))
# print(type(my_dict))

# x=dict()
# print(dict(x))
# print(type(x))

# in-built-method-------------------------

# copy:-
# my_dict={'a':10,'b':20,'c':30,'d':40}
# x=my_dict.copy()
# print(x)

# clear:-
# my_dict={'a':10,'b':20,'c':30,'d':40}
# my_dict.clear()
# print(my_dict)

# update=--------------
# my_dict={'a':50,'b':20,'c':30,'d':40}
# my_dict.update({'b':5,'c':2,'d':1})
# print(my_dict)

# fromkey:- output:-{'a': None, 'b': None, 'c': None, 'd': None}
# my_list=['a','b','c','d']
# my_dict=dict.fromkeys(my_list)
# print(my_dict)

# output:- {'a': 10, 'b': 10, 'c': 10, 'd': 10}
# my_list=['a','b','c','d']
# my_dict=dict.fromkeys(my_list,10)
# print(my_dict)

# my_dict={'a':10,'b':20,'c':30,'d':40}
# # my_dict=dict.fromkeys(my_list,['b'])
# my_dict['a']=50
# print(my_dict('a'))


# my_dict={'b':20,'c':30,'d':40}
# # my_dict.setdefault(key, value)
# my_dict.setdefault('a', None)
# print(my_dict)

# print(dict(my_dict))


# pop():- o/p:- {'b': 50, 'c': 30, 'd': 40}
# my_dict={'a':20,'b':50,'c':30,'d':40}
# my_dict.pop('a')
# print(my_dict)

# popitem:- by difualt last vala le leta tha hai  o/p:- {'a': 20, 'b': 20, 'c': 30}
# my_dict={'a':20,'b':50,'c':30,'d':40}
# my_dict.popitem()
# print(my_dict)

# key():-sari key return in list formate only keys
# my_dict={'a':20,'b':50,'c':30,'d':40}
# print(my_dict.keys())

# values():- sari value print  in list formate 
# my_dict={'a':20,'b':50,'c':30,'d':40}
# print(my_dict.values())

# item():- 
# my_dict={'a':20,'b':50,'c':30,'d':40}
# print(my_dict.items())

# get():-
# my_dict={'a':20,'b':50,'c':30,'d':40}
# print(my_dict.get('a'))
# print(my_dict['a'])

