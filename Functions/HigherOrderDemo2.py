def phonepe():
    print("Pay via Phonepe")

def paytm():
    print("Pay via paytm")

def navi():
    print("Pay via Navi")

def paynow(fun):
    print("Paynow called")
    fun()

appName = input("Enter app name : ")
if appName == "phonepe":
    paynow(phonepe)
elif appName == "paytm":
    paynow(paytm)
elif appName == "navi":
    paynow(navi)
else :
    print("Get lost")