no1 = int(input("Enter No1 :"))
no2 = int(input("Enter No2 :"))

for i in range(no1,no2+1): 
    digits = len(str(i))  
    temp = i
    sum = 0
  
    for j in range(digits):
        r = temp % 10
        fac=1
        for k in range(1,r+1):
            fac = fac * k
        sum = sum + fac
        temp = temp//10

    if i==sum:
        print(i,end=" ")
