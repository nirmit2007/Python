marks = [20,25,34,44]

flag = all(m>15 for m in marks)
print(flag)
flag1 = any(m>25 for m in marks)
print(flag1)

# students = {"amit":23,"summit":24,"raj":23,"ajay":24,"sujay":23}
# bonus = False  >24 [1]
# flag = False  > 20[]

students = {"amit": 23, "summit": 24, "raj": 23, "ajay": 24, "sujay": 23}

bonus = any(age > 24 for age in students.values())  
flag = all(age > 20 for age in students.values())    

print("bonus =", bonus)
print("flag =", flag)
