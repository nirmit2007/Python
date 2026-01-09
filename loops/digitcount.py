no=int(input("Enter No : "))
count=0

while(no>0):
    no = no // 10
    count += 1

print("Digit count = ",count)
