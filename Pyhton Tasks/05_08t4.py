salary = int(input("Enter your salary :"))

# salary       HRA     DA 
# <10000       20%     80% 
# 10000-20000  25%     85%
# above 20000  30%     90%

if(salary < 10000):
    hra = salary * 0.2 
    da = salary * 0.8
    gross_salary = salary + hra + da
    print(" Gross salary :",gross_salary)


elif(salary >= 10000 and salary < 20000):
    hra = salary * 0.25 
    da = salary * 0.85
    gross_salary = salary + hra + da
    print(" Gross salary :",gross_salary)


elif(salary > 20000):
    hra = salary * 0.3 
    da = salary * 0.9
    gross_salary = salary + hra + da
    print(" Gross salary :",gross_salary)