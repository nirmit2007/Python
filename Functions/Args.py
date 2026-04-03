def add(*num):  # stores in tuple
    for i in num:
        flag=True
        if(type(i)!=int):
            return False
        else:
            return True

x=add(1,2)
print(x)
