a=int(input("Enter No1 :"))
b=int(input("Enter No2 :"))
c=int(input("Enter No3 :"))

if(a>b and a>c):
    print("a is large")
elif(a<b and a<c):
    print("a is small")
elif(b>c and b>a):
    print("b is large")
elif(b<c and b<a):
    print("b is small")
elif(a>b and a<c):
    print("a is medium")   
elif(b>a and b<c):
    print("b is medium")
elif(c>a and c<b):
    print("c is medium")    
