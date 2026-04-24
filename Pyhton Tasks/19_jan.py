'''Write a Python Program to Find the Net Salary of Employee using Inheritance.
Create three Class Employee, Perks, NetSalary. Make an Employee class as an abstract class.
Employee class should have methods for following tasks.- To get employee details like employee id, name and salary from user. - To print the Employee details. - return Salary.- An abstract method emp_id.
Perks class should have methods for following tasks.- To calculate DA, HRA, PF. - To print the individual and total of Perks (DA+HRA-PF).
Netsalary class should have methods for following tasks.- Calculate the total Salary after Perks.- Print employee detail also prints DA, HRA, PF and net salary.
Note 1: DA-35%, HRA-17%, PF-12%
Note 2: It is compulsory to create objects and demonstrating the methods with 
              Correct output.                                                                                                                                       Example:
Employee ID: 1
Employee Name: John
Employee Basic Salary: 25000
DA: 8750.0
HRA: 4250.0
PF: 3000.0
Total Salary: 35000.0'''

'''
from abc import ABC, abstractmethod

class Employees(ABC):
    def __init__(self):
        self.Emp_id = None
        self.Name = None
        self.Salary = None

    def get_details(self):
        self.Emp_id = int(input("Employees id :"))
        self.Name = input("Name :")
        self.Salary = int(input("Salary :"))
    
    def print_details(self):
        print(f"Employees id  ={ self.Emp_id }")
        print(f"Employees name  ={ self.Name }")
        print(f"Employees salary  ={ self.Salary }")
    
    @abstractmethod
    def employess_id(self):
        pass


class Perks(Employees):
    def __init__(self):
        super().__init__()
        self.da = 0
        self.hra = 0 
        self.pf = 0

    def cal_perks(self):
        self.da = self.Salary * 0.35
        self.hra = self.Salary * 0.17
        self.pf = self.Salary * 0.12

    def print_perks(self):
        print(f"da  ={ self.da }")
        print(f"hra  ={ self.hra }")
        print(f"pf  ={ self.pf }")

    def employess_id(self):
        return self.Emp_id()


class NetSal(Perks):
    def __init__(self):
        super().__init__()
        self.total_salary = 0
    
    def cal_total_sal(self):
        self.cal_perks()
        self.total_salary = self.Salary + self.da + self.hra - self.pf

    def print_total_salary(self):
        self.print_details()
        self.cal_total_sal()
        print(f"Total Salary: {self.total_salary}")


net_salary = NetSal()
net_salary.get_details()
net_salary.cal_perks()
net_salary.print_perks()
net_salary.print_total_salary()'''




# ---------------------------------------------------------------------------------


'''
Create a program using the instructions given below:
 1.Create a constructor in all three classes (Respondent, Manager and Director) which takes the id and name as input and 
initializes two additional variables, rank and free. rank should be equal to 3 for Respondent, 2 for Manager and 1 for 
Director. free should be a boolean variable with value True initially. (1 mark)
 2.Implement rest of the methods in all three classes in the following way: (2 marks)
 a.receive_call(): prints the message, “call received by (name of the employee)” and sets the free variable to False.
 b.end_call(): prints the message, “call ended” and sets the free variable to True.
 c. is_free(): returns the value of the free variable
 d. get_rank(): returns the value of the rank variable
 3.Create a class Call, with a constructor that accepts id and name of the caller and ini alizes a variable called assigned to 
False. (0.5 marks)
 4.Create a class CallHandler, with three lists, respondents, managers and directors as class variables. (0.5 marks)
 5.Create an add_employee() method in CallHandler class that allows you to add an employee (an object of 
Respondent/Manager/Director) into one of the above lists according to their rank. (1 mark)
 6.Create a dispatch_call() method in CallHandler class that takes a call object as a parameter. This method should find 
the first available employee starting from rank 3, then rank 2 and then rank 1. If a free employee is found, call its 
receive_call() function and change the call’s assigned variable value to True. If no free employee is found, print the 
message: “Sorry! All employees are currently busy.” (2 marks)
 7.Create 3 Respondent objects, 2 Manager objects and 1 Director object and add them into the list of available 
employees using the CallHandler’s add_employee() method. (1 mark)
 8.Create a Call object and demonstrate how it is assigned to an employee. (1 mark)'''

# -------------------------------------------------------

'''Create an abstract class named Shape. 
Create an abstract method named calculate_area for the Shape class.
Create Two Classes named Rectangle and Circle which inherit Shape class.
Create calculate_area method in Rectangle class. It should return the area of the rectangle object. (area of rectangle = 
(length * breadth))
Create calculate_area method in Circle class. It should return the area of the circle object.
(area of circle =πr^2))
Create objects of Rectangle and Circle class.
The python Program Should also check whether the area of one Rectangle object is greater
than another rectangle object .
'''


