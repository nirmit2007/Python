class school : 
    def __init__(self,name,class_0 =0):   
        self.name =name  
        self.class_0 =class_0
    
    def add(self,amt=0,bonus=0):
        self.class_0 += amt +bonus   
        print(f'added {amt} + bonus :{bonus} = {amt +bonus}')
        
    def display(self):
        print(f'name : {self.name} class_0 : {self.class_0}')

class letest(school):
    def __init__(self, name, class_0=0,marks=12):
        super().__init__(name, class_0)
        self.marks = marks
        
    def display(self):
        print(f'letest class info  || class_0 : {self.class_0} || marks : {self.marks}')
        
class current(school):
    def __init__(self, name, class_0=0,marks_limit=100):
        super().__init__(name, class_0)
        self.marks_limit = marks_limit
    
    def display(self):
        print(f'current class info  || class_0 : {self.class_0} || marks_limit : {self.marks_limit}')

s1=letest("saumya",80) 
c1 =current("harshil",90)

# method  overloading  : (same funcation diff arg  )

s1.add(10)
c1.add(5,2) 

# method  overriding  (same name  diff class_0 behaviour )

s1.display()
c1.display()