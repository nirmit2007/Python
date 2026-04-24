'''
TASK 1: Write Data to a Binary File using pickle 
TASK 2: Read Data from Binary File using pickle 
TASK 3: Append Multiple Records in a Binary File 
TASK 4: Read All Records from Binary (Multiple Dumps) 
TASK 5: Search a Student by ID in Binary File 
Problem Statement
Ask the user for a student ID and search in students.dat.
If found → Print record
If not found → Show "Record Not Found" 

TASK 6: Update Marks of a Student in Binary File
Problem Statement
Update marks of an existing student (e.g., id=3) inside students.dat.
Task Requirements
Read all data into a list
Modify the record
Write the updated list back to the same file'''


import pickle

# TASK 1: Write Data to a Binary File using pickle

with open('students.dat', 'wb') as file:
    students = [
        {'id': 1, 'name': 'Alice', 'marks': 85},
        {'id': 2, 'name': 'Bob', 'marks': 90},
        {'id': 3, 'name': 'Charlie', 'marks': 78}
    ]
    pickle.dump(students, file)

# TASK 2: Read Data from Binary File using pickle

with open('students.dat','rb') as f:
    data = pickle.load(f)
    print("TASK 2: Read Data from Binary File")
    print(data)

# TASK 3: Append Multiple Records in a Binary File

with open('students.dat','ab') as f:
    new_std = [
        {'id': 4, 'name' : 'shalin', 'marks' : 88},
        {'id': 5, 'name' : 'rahul', 'marks' : 92}
    ]
    for student in new_std:
        pickle.dump(student, f)     

# TASK 4: Read All Records from Binary (Multiple Dumps)

with open('students.dat','rb') as f:
    try:
        while True:
            student = pickle.load(f)
            print(student)
    except EOFError:
        pass

# TASK 5: Search a Student by ID in Binary File

search_id = int(input("Enter Student ID to search: "))
found = False
with open('students.dat','rb') as f:
    try:
        while True:
            student = pickle.load(f)
            if isinstance(student, list):
                for s in student:
                    if s['id'] == search_id:
                        print("Record Found:", s)
                        found = True
                        break
            else:
                if student['id'] == search_id:
                    print("Record Found:", student)
                    found = True
                    break
    except EOFError:
        pass

if not found:
    print("Record Not Found")