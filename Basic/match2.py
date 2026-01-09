choice = input("Enter yes for entry and no for exit : ")

match choice:
    case "y" | "Y" | "yes" | "YES":
        print("Entry Success")
    case "n" | "N" | "no" | "NO":
        print("Exited...")    
    case _:
        print("INVALID CHOICE")    