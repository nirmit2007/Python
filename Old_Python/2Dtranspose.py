l1= [[1,2,3],
     [4,5,6],
     [7,8,9]]


for i in range(len(l1)):
    l3=[]
    for j in range(len(l1[0])):
        l2 = l1[j][i]
        l3.append(l2)
        print(l3)
    l1[i] = l3

for i in l1:
    print(i)
