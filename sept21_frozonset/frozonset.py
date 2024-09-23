# my_set={'a','b','c','d'}
# my_list=[10,20,30,40,50]
# my_tuple=(10,20,30,40,50)
# new_set=frozenset(my_set)
# print(new_set)
# print(type(new_set))
# print(len(new_set))
# print(max(new_set))
# print(min(new_set))
# print(id(new_set))
# print(sum(new_set))

# operetion:-
a={1,2,3,4,5,6}
b={5,6,7,8,9,10}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
print(type(a.union(b)))
print(type(a.intersection(b)))
print(type(a.difference(b)))
print(type(a.symmetric_difference(b))) 