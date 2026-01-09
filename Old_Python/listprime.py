n=int(input("enter the number :"))
l1=[]
for i in range(n):
    element =int(input("enter the  element : "))
    fc=0
    no=element
    for j in range(1,no+1):
        if(no%j==0):
            fc+=1
    if fc==2:
     l1.append(element)
     print(l1)
    