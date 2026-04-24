accounts={}
logged_in_user =None
account_type =None 
def open_account():
    global accounts,account_type
    username =input("enter the username : ")
    if username in accounts :
        print("account already exists")
        return 
    password =input("enter the password : ")
    # intial balance =25000 
    accounts[username]={
        "password":password,
        "balance":25000,
        "type":account_type
        }
    print("account created successfully")
def login():
    global logged_in_user
    username =input("enter the username : ")
    password =input("enter the  password : ")
    if username in accounts and accounts[username]["password"]==password :
        logged_in_user=username
        print("login successful")
    else :
        print("login failed") 

def deposit():
    global logged_in_user 
    if logged_in_user is None :
        print("you are not logged in")
        return 
    amount =int(input("enter the  amount  you want  to deposit :"))
    accounts[logged_in_user]["balance"] +=amount 
    print("deposit successful")

def withdraw():
    global logged_in_user, account_type
    if logged_in_user is None:
        print("You are not logged in")
        return 

    amount = int(input("Enter the amount you want to withdraw: "))
    account_type = accounts[logged_in_user]["type"]

    if account_type == "savings":
        print(account_type)
        if accounts[logged_in_user]["balance"] - amount >= 10000:
            accounts[logged_in_user]["balance"] -= amount
            print("Withdraw successful")
        else:
            print("Insufficient balance (min ₹10,000 required)")
    
    elif account_type == "current":
        overdraft_limit = -5000
        print(account_type)
        if accounts[logged_in_user]["balance"] - amount >= overdraft_limit:
            accounts[logged_in_user]["balance"] -= amount
            print("Withdraw successful (Overdraft allowed)")
        else:
            print("Insufficient balance (Overdraft limit reached)")

def check_balance():
    global logged_in_user
    if logged_in_user is None :
        print("you are not logged in")
        return 
    account_type=accounts[logged_in_user]["type"]
    print("your balance is :",accounts[logged_in_user]["balance"])

def logout():
    global logged_in_user
    if logged_in_user :
        print("goddbye  thx for using our app")
        logged_in_user=None
    else :
        print("you are not logged in")


def main() :
    global account_type
    while True :
        print("select account type : ")
        print("1. savings account")
        print("2. current account")
        print("3. exit")
        choice =int(input("enter your choice : "))
        if choice ==1 :
            account_type="savings"
            
        elif choice ==2 :
            account_type="current"
        elif choice ==3 :
            break   
        else :
            print("invalid choice")
            continue   
        
        while True :
                    print("1. open account")
                    print("2. login")
                    print("3. deposit")
                    print("4. withdraw")
                    print("5. check balance")
                    print("6. logout")
                    print("7. exit")
                    acc_choice =int(input("enter your choice : "))
                    if acc_choice ==1 :
                        open_account()
                    elif acc_choice ==2 :
                        login()
                    elif acc_choice ==3 :
                        deposit()
                    elif acc_choice ==4 :
                        withdraw()
                    elif acc_choice ==5 :
                        check_balance()
                    elif acc_choice ==6 :
                        logout()
                    elif acc_choice ==7 :
                        break
                    else :
                        print("invalid choice")
main()
