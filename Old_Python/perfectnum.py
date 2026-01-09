n=int(input("Enter No :"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print(n,"is a Perfect Number")
else:
    print(n,"is Not a Perfect Number")