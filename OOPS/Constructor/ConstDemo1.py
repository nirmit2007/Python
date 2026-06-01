#const is special function which has same name as class name
#in python we can create const using __init__(self):
#2 type const default const param const
#const will call when we create an object of class
#use of const is to initilize class in memory

class Match:
    def __init__(self):
        print("Default Constructor Of Match is Called...")
        self.run = 49
        self.wicket = 10

    def getScore(self):
        return self.run,self.wicket

m = Match()        
r,w = m.getScore()
print(r)
print(w)