def demo():
    print("Demo function called")
    return 100

x = demo
print("x",x)
ans = x()
print(ans)

def sum(a,b,c):
    return a+b+c

y = sum
print("y",y)
answer = y(10,20,30)
print(answer)