# user input string  : 

'''a=str(input("Enter your name : "))
b=input("enter the sur-name :")
print(a)
print(b)
print(a+b)
print(type(a))'''   # a ="12" ,b ="78"


# user  input  number  : 


'''a=int(input("enter the  number  : "))
b=int(input("enter the  number  : "))
print(a)
print(b)
print(a+b)'''

"""
a=float(input("enter the  number  : "))
b=float(input("enter the  number  : "))
print(a)
print(b)
"""

"""
task  : 1 ask user to enter the int type number  take a 2 number  and concate them. 
input  a=10 
input b=20
output  c =1020 
"""
"""
a=int(input("enter the  number  : "))
b=int(input("enter the  number  : "))
print(a,end="")
print(b)
"""


#operator : 
"""
1. airthematic : + - * / % // 
2.comparasion  : < > <= >= == !=
3.logic : and or not
4.assignment : +=, -=, *=, /=, %=, //=
5.membership : in ,not in 
"""
# a=12
# b=100
# print(a/b)  # division  : 3.33333 
# print(a//b)  # floor division 

# print(a!=b)

# print(a==b or a>b)

# a=a+b 
# a+=b
# print(a)

"""l1=[1,2,3,4,5,"ketan"]
print("meet" not  in l1)
"""

"""
conditional statement  : 

if condition :
    statement/print 
else :
    statement/print

"""

# a=int(input("enter the  number  : "))
# b=int(input("enter the  number  : "))

"""if a>b:
    print("a is big")
else :
    print("b is  big")

"""    
"""
if a>b :
    print("a is big")
if b>a :
    print("b is big")
"""

# ladder if : 

"""
syntax : 

if con:
    statement
elif con :
    statement
else :
    statement
"""

"""
a=int(input("enter the  number  : "))
b=int(input("enter the  number  : "))
c=int(input("enter the  number  : "))

if a>b and a>c :
    print("a is big")
elif b >a and b>c :
    print("b is big")
elif c>a and c>b :
    print("c is big")
else :
    print("same")
"""

# nested : 
"""
if con : 
    if con :
        statement
    else :
        statement
elif con :
    if con :
        statement
    else :
        statements
"""
"""
a=int(input("enter the  number  : "))
b=int(input("enter the  number  : "))
c=int(input("enter the  number  : "))

if a>b :
    if a>c :
        print("a is big")
    else :
        print("c is big")
elif b>a :
    if b>c :
        print("b is big")
    else :
        print("c is big")
else:
    print("same")
"""

"""
task  :2 

ask user to enter the three number  and  check which number is small medium or large. 
input a=20 
input b=20
input c=30

output  : a is  small b is   medium c is large

task  :3 
ask user to enter the character and convert into lowercase or uppercase and vice versa.

input : a 
output :A 

"""

# a=100 b=20 c=300
"""
if a>b and a>c  : 
    print("a is big") 
    if b>c :
        print("b is medium")
    else :
        print("c is small")

"""

#task :3   A =ascci value : 65   a  = 97  diff =32 

# function  : ord 
ch=input("enter the character : ") # t

'''if ch >='A' and ch <='Z': 
    ch=ord(ch)+32 
    print("lower case :",chr(ch))
else :
    ch=ord(ch)-32
    print("upper case :",chr(ch))
'''

# task :4 

"""
ask user to enter the salary  and calculate the gross salary . 

salary       HRA     DA 
<10000       20%     80% 
10000-20000  25%     85%
above 20000  30%     90%

gross salary  = salary  + HRA +DA 

hra = salary  * percent
da = salary  * percent

ex : salary =9000 
hra = salary * percent = 9000 *0.20 =1800 
da = salary  * percent = 9000 *0.80 =7200 
gross = salary  + hra +da =9000 + 1800 +7200 =18000 

"""