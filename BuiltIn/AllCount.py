s1=input("Enter String : ")
digit=0
sc=0
ch=0
sum=0
for i in s1:
    if i.isdigit():
        digit+=1
        sum = sum + int(i)
        print("Sum = ",sum)
    elif i.isalpha():
        ch+=1
    else:
        sc+=1

print("Total Digits = ",digit)
print("Total Characters = ",ch)
print("Total Special Ch. = ",sc)


