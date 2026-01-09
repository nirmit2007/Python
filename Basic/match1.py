choice = int(input(f"Enter 1 For Add \n Enter 2 For Sub"))

match(choice):
    case 1:
        print("Addition Completed...")
    case 2:
        print("Substraction Completed...")
    case _:
        print("Invalid choice...")