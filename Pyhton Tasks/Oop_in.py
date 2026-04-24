class student():
    def show(self):
        print("a student.")

class teacher(student):
    def show1(self):
        print("a teacher.")

class principal(teacher):
    def show2(self):
        print("a principal.")

p=principal()
p.show()
p.show1()
p.show2()