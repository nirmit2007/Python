no1=int(input("Enter No1 : "))
no2=int(input("Enter No2 : "))

max = None
min = None

if no1>no2:
    max=no1
    min=no2
    print("Max is : ",max)
    print("Min is : ",min)

else:
    min=no2
    max=no1
    print("Max is : ",max)
    print("Min is : ",min)

    