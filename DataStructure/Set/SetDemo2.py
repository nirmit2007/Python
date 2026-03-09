data = {"ram","krishna","arjun"}

data.pop()  # it will remove word randomly
print(data)

data.remove("ram") #error if ele is not present
print(data)

data.discard("krishn") # if ele not present it will not give error 
print(data)

