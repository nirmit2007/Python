"""
home work : 

input  :1 
Original dictionary: sort by value asc to desc

d1 = {'name1': 'Theodore', 'name2': 'Mathew', 'name4': 'Roxanne', 'name3': 'David'}
output : {'name3': 'David', 'name2': 'Mathew', 'name4': 'Roxanne','name1': 'Theodore'}
"""

d1 = {'name1': 'Theodore', 'name2': 'Mathew', 'name4': 'Roxanne', 'name3': 'David'}
d2 ={}

for i in sorted(d1.values()):
    print(i, end=" ")

    for name, value in d1.items():
        if value == i:
            d2[name] = value

print(d2)