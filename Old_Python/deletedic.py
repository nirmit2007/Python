'''Remove a Key from a Dictionary 
ask user to enter the  key  which  user want to delete 
myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
output : {'b': 2, 'c': 3, 'd': 4}'''

d1={'a': 1, 'b': 2, 'c': 3, 'd': 4}
key=input("Enter Key : ")
d1.pop(key)
print(d1)