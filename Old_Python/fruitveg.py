total_bill = 0 

while True:
    print("1. FRUITS")
    print("2. VEGETABLES")
    print("3. Exit")

    choice = int(input("Enter the choice: "))

    match choice:
        case 1:
            print("1. APPLE rs: 100")
            print("2. KIWI rs: 150")
            print("3. ORANGE rs: 90")
            subchoice = int(input("Enter the subchoice: "))
            match subchoice:
                case 1:
                    print("You selected apple")
                    qty = int(input("Enter the quantity: "))
                    total_bill += 100 * qty
                case 2:
                    print("You selected kiwi")
                    qty = int(input("Enter the quantity: "))
                    total_bill += 150 * qty
                case 3:
                    print("You selected orange")
                    qty = int(input("Enter the quantity: "))
                    total_bill += 90 * qty

        case 2:
            print("1. POTATOES rs: 60")
            print("2. TOMATO rs: 40")
            print("3. METHI rs: 10")
            subchoice = int(input("Enter the subchoice: "))
            match subchoice:
                case 1:
                    print("You selected potatoes")
                    qty = int(input("Enter the quantity: "))
                    total_bill += 60 * qty
                case 2:
                    print("You selected tomato")
                    qty = int(input("Enter the quantity: "))
                    total_bill += 40 * qty
                case 3:
                    print("You selected methi")
                    qty = int(input("Enter the quantity: "))
                    total_bill += 10 * qty

        case 3:
            break

print("Your total bill =", total_bill)
