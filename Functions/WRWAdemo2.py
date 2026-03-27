#2)accept list as argument and return sum of list  dont use builtin sum function..

def list(l1):
    sum = 0
    for i in l1:
        sum += i
    return sum

ans = list([10,20,30])
print(ans)