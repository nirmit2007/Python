class demo:

    x = 100 # we can access it anywhere (class level static variable)

    def test(self):
        print("Nirmit",self)
        print("Test Function of Demo Class is Called...")
        self.no1 = 16 #instance variable... not local (access directly)
        no2 = 200 # local variable (not accesible directly)

        def call(self):
            print(self.no1)    
            #print(self.no2) it is local variable test it can use inside test only


d = demo() #demo class object
d.test() #it will pass class current object in param by default d.test(d)
print(d.x)
#print(demo.x)

d.call()
print(d.no1)