'''ask user to enter the  3  subjects  marks  and  calculate percentage and  given grade. 

percentage    grade 
90             A+ 
80 -90         A 
70 -80         B+ 
60 -70         B 
50 -60         C+ 
40 -50         C
below 40       fail'''

a=int(input("Enter Maths Marks:"))
b=int(input("Enter Physics Marks:"))
c=int(input("Enter Chemistry Marks:"))

total = a+b+c
avg = total/3

if avg>=90:
    print("Grade = A+")
elif avg>=80 and avg<=90:
    print("Grade = A")
elif avg>=70 and avg<=80:
    print("Grade = B+")    
elif avg>=60 and avg<=70:
    print("Grade = B")
elif avg>=50 and avg<=60:
    print("Grade = C+")
elif avg>=40 and avg<=50:
    print("Grade = C")
else:
    print("You are Fail")    