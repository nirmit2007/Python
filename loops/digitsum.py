no=int(input("Enter No : "))
sum=0
temp=0

while(no!=0):
    temp = no % 10
    sum = sum + temp
    no = no // 10

print("Sum of digit = ",sum)