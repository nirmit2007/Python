l1 =[[1,2,3],[4,5,6],[7,8,9]]

# 1. For Loop

for i in range(len(l1)):
    for j in range(len(l1[i])):
        print(l1[i][j],end=" ")
    print()

# 2. For Each

for i in l1:
    for j in i:
        print(j,end=" ")
    print()