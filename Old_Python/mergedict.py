'''Merge Two Python Dictionaries 
input : d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200} 

ouptut : {'x': 300, 'y': 200, 'a': 100, 'b': 200}'''

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}

d1.update(d2)
print(d1)