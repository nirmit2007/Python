minbalance=10000
attempts=3

while attempts > 0:
    balance = int(input("Enter Your Bank Balance : "))

    if balance >= minbalance:
        print("Balance Accepted")
        break
    else:
        attempts -= 1
        print("Minimum balance should be 10000")
        print("Attempts left:", attempts)

if attempts == 0:
    print("Account blocked. Try again later.")