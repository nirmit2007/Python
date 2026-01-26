color = ["red","yellow","green","blue","red","red","green"]
dup = []
r = []
count=0

for i in color:
    if i not in dup:
        dup.append(i)
    else:
        r.append(i)
        count+=1
print(r)
print(count)