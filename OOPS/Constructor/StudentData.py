from datetime import datetime

class Student:
    def __init__(self,rno,name):
        self.rno = rno
        self.name = name

    def attendance(self):
        f = open("OOPS/Constructor/attendance.txt","a")
        f.write(str(self.rno) + " " + self.name + " " + str(datetime.now()) + "\n")
        f.close()

for i in range(5):
    rno = int(input("Enter Roll No : "))
    name = input("Enter Name : ")

    s = Student(rno,name)
    s.attendance()