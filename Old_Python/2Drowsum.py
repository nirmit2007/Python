l1= [[1,2,3],
     [4,5,6],
     [7,8,9]]

for i in range(len(l1)):
    sum = 0
    for j in range(len(l1[0])):
       sum = sum + l1[i][j]
       
    print(sum)