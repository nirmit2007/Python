# create school data
# school has 3 std: 10, 11, 12
# every std has 5 students

# 1) find common name student from all std
# 2) give all students name
# 3) give only unique students name

school = {
            "std10": {"Rahul", "Amit", "Priya", "Neha", "Karan"},
            "std11": {"Amit", "Priya", "Riya", "Soham", "Jay"},
            "std12": {"Priya", "Amit", "Arjun", "Kiran", "Riya"} 
         }

common_students = school["std10"].intersection(school["std11"], school["std12"])
print("Common students:", common_students)

all_students = school["std10"].union(school["std11"], school["std12"])
print("All students:", all_students)

unique_students = school["std10"].symmetric_difference(school["std11"]).symmetric_difference(school["std12"])
print("Unique students:", unique_students)

