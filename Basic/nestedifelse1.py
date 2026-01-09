age = int(input("Enter Your Age : "))

if age>18:
    print("you are elidible for voting")
    if age>=21:
        print("you are elidible for marriage")
    else: 
        print("you are not elidible for marriage") 
else:
    if age>6:
        print("you can go to school")
    else:
        print("Gher Bhega")    