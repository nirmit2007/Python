'''
Dictionary :

Dictionary is a collection of elements in key-value pair format.
Dictionary does NOT allow duplicate keys (but values can be duplicate).
Dictionary stores data using keys (not index).
Dictionary is heterogeneous (can store different data types).
Dictionary is iterable (we can use loop).
Dictionary is subscriptable using keys.
Dictionary is mutable (we can add, update, delete elements).
Data type of dictionary is dict.
We can declare dictionary using {} braces.
Dictionary is dynamic in size.'''

dict = {1:"Nirmit",2:"Khushi",3:"Vidhi",4:True}
print(dict)

print(dict[4]) #if key is not present it will throw exception (error)
print(dict.get(5)) #""  ""  None



k = dict.keys() #list
print(k)
v = dict.values() #values
print(v)

kv = dict.items()
print(kv)

for i,j in dict.items():
    print(f"{i} - {j}")