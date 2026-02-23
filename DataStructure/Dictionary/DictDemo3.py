d1 = {1:"Nirmit",2:"Khushi",3:"Vidhi"}

print(d1.get(1)) 
print(d1[2]) 


#remove..
if 3 in d1:
    removedValue = d1.pop(3) #101-raj
    print("removing...",removedValue)
else:
    print("not availlable to remove...")    

print(d1)

