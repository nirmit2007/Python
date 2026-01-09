while True:

    a=int(input("enter the  number  : "))
    b=int(input("enter the  number  : "))

    while True:

        print("1. addition")
        print("2. subtraction")
        print("3. multiplication")
        print("4. division")
        print("5. modulus")
        print("6. floor division")
        print("7. Exit")


        choice =int(input("enter the choice : "))

        match choice:
            case 1 :
                print(a+b)
            case 2 :
                print(a-b)
            case 3 :
                print(a*b)
            case 4 :
                print(a/b)
            case 5 :
                print(a%b)
            case 6 :
                print(a//b)
            case 7 :
                print("Thank you")
                break    
            case _ :
                print("Invalid Choice")    
            