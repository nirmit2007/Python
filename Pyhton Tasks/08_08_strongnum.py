num = int(input("Enter number :"))
temp = num
sum = 0
fact = 1
digits = len(str(num))
for i in range(0 , digits):
    r = temp % 10
    fact = 1
    for j in range(1,r+1):
        fact = fact * j
    sum = sum + fact
    temp = temp // 10
print(sum)

if sum == num:
    print("it is a strong number")
else:
    print("Not strong number")