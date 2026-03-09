data1 = {"ram","seeta","lakshman","kush","luv","krishna"}
data2 = {"ram","arjunn","bhim","sahdeve","krishna","draupadi"}

x = data1.union(data2) # it will remove dup values and combine both sets
#x = data1 | data2
print(x)

x = data1.intersection(data2) # it will give common values
print(x)

x = data1.difference(data2) # it will give values which are present in data1 but not in data2
print(x)

x = data1.symmetric_difference(data2) # it will give values which are present in data1 and data2 but not common
print(x)

y = data1.issuperset(data2) # it will check if data1 is superset of data2 or not if all values of data2 are present in data1 then it will return true otherwise false
print(y)

y = data1.issubset(data2) # it will check if data1 is subset of data2 or not if all values of data1 are present in data2 then it will return true otherwise false
print(y)