import datetime as dt

login_data={}
bank_data={}
usr_name=""



def signup():
    print("\nSignup:-")
    user_name = input("\nEnter the username: ")
    passwd = input("Enter the password: ")
    print("\nSignup Successful!!\n")
    login_data[user_name] = passwd
    bank_data[user_name] = 10000


def login():
    global usr_name
    count = 0
    print("\nLogin:-")
    user_name = input("\nEnter your username: ")
    if user_name in login_data:
        while count<3:
            passwd = input("\nEnter the password: ")
            if login_data[user_name]==passwd:
                print("\nLogin Successful!!\n")
                usr_name = user_name
                create_passbook()
                count = 3
                return 1
                
            elif count<2:
                print("\nInvalid password, Try again.")
                count+=1
                print("Attempts remaining:",(3-count))
            else:
                print("\nAccount locked, Try again later.\n")
                count+=1
                return 2
    else:
        return 3


def withdraw_amt():
    amt = int(input("\nEnter the amount you want to withdraw: $"))
    if amt < bank_data[usr_name] and (bank_data[usr_name] - amt) >=10000:
        print(f"${amt} withdrawn successfully!!")
        bank_data[usr_name] -= amt
        update_passbook(1,amt)
    else:
        print("\nInsufficient funds to withdraw!!\n")


def deposit_amt():
    amt = int(input("\nEnter the amount you want to deposit: $"))
    if amt > 50:
        print(f"\n${amt} deposited successfully!!\n")
        bank_data[usr_name] += amt
        update_passbook(2,amt)
    else :
        print("\nInvalid input, minimum amount to deposit is $50.\n")


def check_balance():
    print(f"\nAccount Balance: ${bank_data[usr_name]}\n")



def create_passbook():
    with open("bank.txt", "w") as bank:
        bank.write("\t\t\t\tSTATE BANK OF INDIA\n\n")
        # Date and account name on same line, aligned with tabs
        bank.write(f"Date: {dt.datetime.now().strftime('%d-%m-%y')}\t\t\t\t\t\t\tACC.NAME: {usr_name}\n")
        bank.write("BRANCH: AHMEDABAD\n\n")
        # Column headers aligned with tabs
        bank.write("DATE/TIME\t\t\t\tAMOUNT\t\t\tDR\t\t\tCR\t\t\tBALANCE\n")
        bank.write("-" * 75 + "\n")
        # First / opening entry (date/time and balance)
        bank.write(f"{dt.datetime.now().strftime('%d-%m-%y/%H:%M:%S')}\t\t\t\t\t\t\t\t\t\t\t\t{bank_data[usr_name]}\n")


def update_passbook(flag, amount):
    """
    flag == 1 -> debit (AMOUNT and DR filled)
    flag == 2 -> credit (AMOUNT and CR filled)
    """
    timestamp = dt.datetime.now().strftime('%d-%m-%y/%H:%M:%S')
    with open("bank.txt", "a") as bank:
        if flag == 1:
           
            bank.write(f"{timestamp}\t\t{amount}\t\t\t{amount}\t\t\t\t\t{bank_data[usr_name]}\n")
        elif flag == 2:
            
            bank.write(f"{timestamp}\t\t{amount}\t\t\t\t\t\t{amount}\t\t{bank_data[usr_name]}\n")




    
def operation():
    
    while True:
        print("1---> Withdraw amount\n2---> Deposit amount\n3---> Check Balance\n4---> Logout\n")
        operation_choice = int (input("\nEnter your choice: "))

        if operation_choice == 1:
            withdraw_amt()
        elif operation_choice == 2:
            deposit_amt()
        elif operation_choice == 3:
            check_balance()
        elif operation_choice == 4:
            print("\nAccount logged out successfully!!\n")
            break
        else:
            print("\nInvalid choice!!\n")



while True:

    print("1---> Login\n2---> Signup")
    usr_choice = int(input("\nEnter your choice: "))

    if usr_choice == 1:
        value = login()
        if value == 1:
            operation()
            break
        elif value == 2:
            continue
        elif value == 3:
            print("\nAccount with this username does not exist, please signup first.\n")

    elif usr_choice == 2:
        signup()
        value = login()
        if value == 1:
            operation()
            break
        elif value == 2:
            continue
        elif value == 3:
             print("\nInvalid username, Try again.\n")

    else:
        print("\nInvalid Choice!!\n")