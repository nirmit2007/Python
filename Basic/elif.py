no1=int(input("Enter No1 :"))
no2=int(input("Enter No2 :"))
no3=int(input("Enter No3 :"))

if(no1>no2):
    print(no1,"is greater than",no2)
elif(no2>no3):  
    print(no2,"is greater than",no3)
elif(no3>no1):
    print(no3,"is greater than",no1)
elif(no1==no2==no3):
    print("All are equal")    
