start = int(input("Enter the starting number :"))
end = int(input("Enter the ending number :"))


for i in range(start,end+1):  # 145 , 1001
    digits = len(str(i))    #3
    temp = i 
    sum = 0
                       #145
    for j in range(digits):       # 0 , 3
        r = temp % 10           #   145 % 10 == 5
        fact = 1
        for k in range(1,r+1):     # 1,6
            fact = fact * k         #1
        sum = sum + fact            #
        temp = temp // 10   #145 // 10 = 14
    if i == sum:
        print(i,end=" ")