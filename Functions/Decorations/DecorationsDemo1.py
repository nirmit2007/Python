#decorators are pure python function which is use for change function behaviour without
#change of code
#deco.. are expecting func as argument, and decor.. will return inner function object
#deco will use @above function

def OpenPayment_App(func):
    print(func)

    def inner():
        print("Opening Paymnet Application...")
        func()
    return inner



@OpenPayment_App

def paymentApp():
    print("Payment App Function Called")

paymentApp()