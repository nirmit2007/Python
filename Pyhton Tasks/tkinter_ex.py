import tkinter  as tk 
from tkinter import messagebox 

class student :
    def __init__(self,rollno,name,marks):
        self.rollno = rollno
        self.name=name 
        self.marks=marks
    
    def display(self):
        return f"{self.rollno},{self.name},{self.marks}\n"
        
class filemanager : 
    FILE ="25_fullday.txt"
    
    @staticmethod 
    def read_all():
        try :
            with open(filemanager.FILE,"r") as f :
                return f.readlines() 
        except FileNotFoundError:
            return [] 

    @staticmethod 
    def write_all(lines):
        with open(filemanager.FILE,"w") as f :
            f.writelines(lines)

    @staticmethod 
    def add_student(obj):
        with open(filemanager.FILE,"a") as f :
            f.write(obj.display())
    
    @staticmethod 
    def delete_student(rollno):
        lines = filemanager.read_all()
        with open(filemanager.FILE,"w") as f :
            for line in lines :
                if line.strip("\n").split(",")[0] != str(rollno):
                    f.write(line)

    @staticmethod 
    def search_student(rollno):
        # use read_all() to avoid FileNotFoundError
        lines = filemanager.read_all()
        for line in lines :
            if line.strip("\n").split(",")[0] == str(rollno):
                return line 
        return None

    @staticmethod
    def update_student(obj):
        # use read_all() so missing file is handled
        lines = filemanager.read_all()

        updated = []
        replaced = False
        for line in lines:
            if line.strip("\n").split(",")[0] == str(obj.rollno):
                updated.append(obj.display())   # replace old record
                replaced = True
            else:
                updated.append(line)

        filemanager.write_all(updated)

class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")

        # Labels and Entries
        tk.Label(root, text="Roll No").grid(row=0, column=0)
        tk.Label(root, text="Name").grid(row=1, column=0)
        tk.Label(root, text="Marks").grid(row=2, column=0)

        self.rollno_entry = tk.Entry(root)
        self.name_entry = tk.Entry(root)
        self.marks_entry = tk.Entry(root)

        self.rollno_entry.grid(row=0, column=1)
        self.name_entry.grid(row=1, column=1)
        self.marks_entry.grid(row=2, column=1)

        # Buttons
        tk.Button(root, text="Add Student", command=self.add_student).grid(row=3, column=0)
        tk.Button(root, text="Delete Student", command=self.delete_student).grid(row=3, column=1)
        tk.Button(root, text="Search Student", command=self.search_student).grid(row=4, column=0)
        tk.Button(root, text="Update Student", command=self.update_student).grid(row=4, column=1)

    def add_student(self):
        rollno = self.rollno_entry.get()
        name = self.name_entry.get()
        marks = self.marks_entry.get()
        student_obj = student(rollno, name, marks)
        filemanager.add_student(student_obj)
        messagebox.showinfo("Info", "Student added successfully!")

    def delete_student(self):
        rollno = self.rollno_entry.get()
        filemanager.delete_student(rollno)
        messagebox.showinfo("Info", "Student deleted successfully!")

    def search_student(self):
        rollno = self.rollno_entry.get()
        result = filemanager.search_student(rollno)
        if result:
            messagebox.showinfo("Info", f"Student Found: {result}")
        else:
            messagebox.showinfo("Info", "Student not found!")

    def update_student(self):
        rollno = self.rollno_entry.get()
        name = self.name_entry.get()
        marks = self.marks_entry.get()
        student_obj = student(rollno, name, marks)
        filemanager.update_student(student_obj)
        messagebox.showinfo("Info", "Student updated successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()
