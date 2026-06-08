class Father:

    def __init__(self):
        print("Father Class Called...")
        self.amount = 0
        self.a = 100

class Mother:

    def __init__(self):
        print('Mother Class Called...')
        self.amount = 1
        self.b = 200
    
class Child(Mother,Father):

    def __init__(self):
        super().__init__()
    
    def getInfo(self):
        print("Amount : ",self.amount)
        print("B : ",self.b)

c = Child()
c.getInfo()