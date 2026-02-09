'''
tuple:
tuple is collection of elements
tuple allows duplicate elements
tuple is hetrogenious
tuple stores data in index
tuple is iterable: loop
tuple is supscritable:
tuple is immutable ----------------------> Key Point
data type of tuple is tuple
we can decalre tuple using () braces
tuple is dynamic in size'''

t1 = ()
print(type(t1))
print(type(t1).__name__)

name = ("nirmit","vidhi","khushi")
print(name[0])

x = name.count("vidhi")
print(x)

x1 = name.index("khushi")
print("index...",x1)


#immutable...

#users[0] = "RAM" #TypeError: 'tuple' object does not support item assignment
#users[0]="ram"