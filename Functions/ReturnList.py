'''data(.........)
return all keys as list ...

data(name=ajay,age2=3)'''

def data(**mydata):
    return list(mydata.keys())

a = data(name="nirmit",age=18,id=123)
print(a)