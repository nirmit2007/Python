def phonepe(amount):
    print("Pay via Phonepe")
    print("Amount = ",amount)

def paytm(amount):
    print("Pay via paytm")
    print("Amount = ",amount)

def navi(amount):
    print("Pay via Navi")
    print("Amount = ",amount)

def paynow(fun,amount):
    print("Paynow called")
    fun(amount)

appName = input("Enter app name : ")
amount = int(input("Enter amount : "))

if appName == "phonepe":
    paynow(phonepe,amount)
elif appName == "paytm":
    paynow(paytm,amount)
elif appName == "navi":
    paynow(navi,amount)
else :
    print("Get lost")