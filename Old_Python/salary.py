'''ask user to enter the salary  and calculate the gross salary . 

salary       HRA     DA 
<10000       20%     80% 
10000-20000  25%     85%
above 20000  30%     90%

gross salary  = salary  + HRA +DA 

hra = salary  * percent
da = salary  * percent'''

a=int(input("Enter Salary :"))

if a<1000:
    hra = a * 0.2    
    da = a * 0.8
    gross_salary = a + hra + da
    print("Gross Salary :",gross_salary)

elif(a>=10000 and a<=20000):
    hra = a * 0.25    
    da = a * 0.85
    gross_salary = a + hra + da
    print("Gross Salary :",gross_salary)

elif(a>=20000):
    hra = a * 0.30    
    da = a * 0.90
    gross_salary = a + hra + da
    print("Gross Salary :",gross_salary)