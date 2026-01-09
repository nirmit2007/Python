no=int(input("Enter No :"))
digits=len(str(no))
sum = 0
multy = 1
dup=no
for i in range (digits):
    temp = no % 10
    sum = sum + temp
    multy = multy * temp
    no = no//10


if sum==multy:
    print(dup,"is Twin")
else:
    print(dup, "is not Twin")