# python directly cannot support Overloading

from multipledispatch import dispatch

class Bank:

    def __init__(self):
        print("Bank Class Constructor Called...")

    @dispatch(int,int)
    def deposit(self,a,b):
        print(a,b)

    @dispatch(int)
    def deposit(self,a):
        print(a)
    
b = Bank()
b.deposit(100,200)
b.deposit(100)
