'''set:
set is collection of elements
set does not allows duplicate elements
set is hetrogenious
set stores data in hash
set is iterable: loop
set is not supscritable:
set is mutable
data type of set is set
we can decalre list using {} braces
set is dynamic in size
set is unordered..
'''

data = {}                  # it gives dict datatype
print(type(data))

data = set()  # it gives set datatype
print(type(data))

data = {1,6,1900,1000,2,22,3,4,4,5}
print(data)
print(type(data))

#print(data[0]) error.. # there is no index in set

for i in data:
    print(i)