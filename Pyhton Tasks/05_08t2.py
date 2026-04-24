a = int(input("Enter the number :"))
b = int(input("Enter the number :"))
c = int(input("Enter the number :"))

if(a > b and a > c):
    print("a is largest")
    if(b > c) :
        print("b is medium")
    elif(c > b):
        print("c is medium")
    else:
        print("B and C are same")
elif(b > a and b > c):
    print("b is largest")
    if(a > c):
        print("a is medium")
    elif(c > a):
        print("c is medium")
    else:
        print("a and c are same")
elif(c > a and c > b):
    print("c is largest")
    if(a > b):
        print("a is medium")
    elif(b > a):
        print("b is medium")
    else:
        print("Same")

if(a < b and a < c):
    print("A is smallest")
elif(b < a and b < c):
    print("b is smallest")
else:
    print("c is smallest")
    