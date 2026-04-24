d1 = {}

def add_emp():
    sr_no = int(input("Enter serial number: "))
    name = input("Enter name: ")
    salary = int(input("Enter salary: "))
    d1[sr_no] = {name, salary}
    print("Employee added successfully.")

def remove_emp():
    sr_no = int(input("Enter serial number to remove: "))
    if sr_no in d1:
        del d1[sr_no]
        print("Employee removed successfully.")
    else:
        print("Employee not found.")

def update_emp():
    sr_no = int(input("Enter serial number to update: "))
    if sr_no in d1:
        x = int(input("Enter 1 to update name, 2 to update salary, 3 to update both: "))
        if x == 1:
            name = input("Enter new name: ")
    
            d1[sr_no] = {name}
            print("Employee name updated successfully.")
        elif x == 2:
            salary = int(input("Enter new salary: "))
            d1[sr_no] = {salary}
            print("Employee salary updated successfully.")

        elif x == 3:
            name = input("Enter new name: ")
            salary = int(input("Enter new salary: "))
            d1[sr_no] = {name, salary}
            print("Employee details updated successfully.")
    else:
        print("Employee not found.")

def search_emp():
    sr_no = int(input("Enter serial number to search: "))
    if sr_no in d1:
        print(f"Employee found: Serial Number: {sr_no}, Details: {d1[sr_no]}")
    else:
        print("Employee not found.")


def display_emp():
    if not d1:
        print("No employees to display.")
        return
    for sr_no, details in d1.items():
        name, salary = details
        print(f"Serial Number: {sr_no}, Name: {name}, Salary: {salary}")


def main():
    while True:
        print("\nMenu:")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Update Employee")
        print("4. Search Employee")
        print("5. Display All Employees")
        print("6. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            add_emp()
        elif choice == 2:
            remove_emp()
        elif choice == 3:
            update_emp()
        elif choice == 4:
            search_emp()
        elif choice == 5:
            display_emp()
        elif choice == 6:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")