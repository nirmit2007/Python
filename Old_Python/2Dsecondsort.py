l1 = [[1,2],[3,0],[2,1]]

# output = [[3,0],[2,1],[1,2]]

for i in range(3):  
        for j in range(i+1,3):    
                if l1[i][1] > l1[j][1]:
                   temp = l1[i]
                   l1[i] = l1[j]
                   l1[j] = temp
print(l1)


