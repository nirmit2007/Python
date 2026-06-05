from datetime import datetime
class User:

    def __init__(self,name):
        self.name = name

class Employee(User):

    def __init__(self, name):
        super().__init__(name)

    def save(self):
        f = open("OOPS/Inheritance/Employee.txt","a")
        f.write(self.name + " " + str(datetime.now()) + "\n")
        f.close()

class Manager(User):

    def __init__(self, name):
        super().__init__(name)

    def save(self):
        f = open("OOPS/Inheritance/Manager.txt","a")
        f.write(self.name + " " + str(datetime.now()) + "\n")
        f.close()

for i in range(2):
    name = input("Enter Employee Name : ")
    e = Employee(name)
    e.save()

for i in range(2):
    name = input("Enter Manager Name : ")
    m = Manager(name)
    m.save()



        