def list(l1):
    max = l1[0]

    for i in l1:
        if i>max:
            max = i
    return max

ans = list([10,20,30])
print("Max = ",ans)