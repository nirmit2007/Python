'''Create a login system. Input username and password. Check if they match predefined values. Also:

Block login after 3 wrong attempts

Show "Account locked" after 3 failed tries'''


username="Nirmit"
password="2007"
attempts = 0

while attempts < 3:

        u_input = input("Enter username: ")
        p_input = input("Enter password: ")

        if u_input == username and p_input == password:
            print("Login successful!")
            break
        else:
            print("Login failed.")
            attempts += 1


if attempts == 3:
    print("Account locked.")
    