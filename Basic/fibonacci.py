# 0 1 1 2 3 5 8 13 21.....

no = int(input("Enter number of Fibonacci numbers: "))

a, b = 0, 1

for i in range(no):
    if i == 0:
        print(a, end=" ")
    elif i == 1:
        print(b, end=" ")
    else:
        c = a + b
        print(c, end=" ")
        a = b
        b = c
        
        
