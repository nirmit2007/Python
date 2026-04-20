def loginRequired(func):
    def inner(*args,role):
        if role in args:
            print("Netflix Opened")
            func(args,role=role)
        else:
            print("Sorry Netflix not accessible:")    
    return inner


@loginRequired
def accessHomePage(*args,role):
    print("Welcome to Netflix by ",role)
accessHomePage("nirmit","khushi","vidhi",role="nirmit")    


@loginRequired
def accessCartPage(*args,role):
    print("accesing cart by",role)
accessCartPage("nirmit","khushi","vidhi",role="vidhi")


accessHomePage("nirmit","khushi","vidhi",role="vidhi")    
accessCartPage("nirmit","khushi","vidhi",role="khushi")  