# task  :2 
"""
ask user to  enter the  two string and  interchange  the  first three letter . 

input  1 :color 
input  2 :full

output :1 fulor 
oupput :2 coll
"""

a=input("Enter a : ")
b=input("Enter b : ")

print(b[0:3]+a[3:])
print(a[0:3]+b[3:])