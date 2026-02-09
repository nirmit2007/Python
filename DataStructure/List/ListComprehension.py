# 1. Using Name
l1 = ["nirmit","khushi","vidhi"]
initcap=[]

initcap = [i.capitalize() for i in l1]
print(initcap)

#2. Using Numbers

l2 = [100,200,300,400,500]
sub=[]

sub = [i-100 for i in l2]
print(sub)

#3. Using Loops

l3 = []

cube = [i**3 for i in range(1,6)]
print(cube)