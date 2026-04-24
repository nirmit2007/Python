city=(input("enter grade of your city (A,B,C,D,E,F)"))
citytype=int(input("enter city type 1 for metro, 2 for tier 2, 3 for tier 3"))
# FORMULA  : Gross Pay = Basic Pay + HRA + DA + Other Allowances + TA - (Professional Tax + EPF)

if(city=="A" and citytype==1):
     BasicPay=60000
     Grosspay=BasicPay + (0.3 * BasicPay)+(0.5 *BasicPay)+8000+ 900-(200+(0.11*BasicPay) )
     print("Gross Pay of employee is:",Grosspay)
     print("Annual Income of employee is:",Grosspay*12)
elif(city=="A" and citytype==2):
    BasicPay=60000
    Grosspay=BasicPay + (0.2* BasicPay)+(0.5 *BasicPay)+8000+ 900-(200+(0.11*BasicPay) )
    print("Gross Pay of employee is:",Grosspay)
    print("Annual Income of employee is:",Grosspay*12)
elif(city=="A" and citytype==3):
    BasicPay=60000
    Grosspay=BasicPay + (0.2* BasicPay)+(0.5 *BasicPay)+8000+ 900-(200+(0.11*BasicPay) )
    print("Gross Pay of employee is:",Grosspay)
    print("Annual Income of employee is:",Grosspay*12)
elif(city=="B" and citytype==1):
    BasicPay=50000
    Grosspay=BasicPay + (0.3* BasicPay)+(0.5 *BasicPay)+7000+ 900-(200+(0.11*BasicPay) )
    print("Gross Pay of employee is:",Grosspay)
    print("Annual Income of employee is:",Grosspay*12)
elif(city=="B" and citytype==2):
    BasicPay=50000
    Grosspay=BasicPay + (0.2* BasicPay)+(0.5 *BasicPay)+7000+ 900-(200+(0.11*BasicPay) )
    print("Gross Pay of employee is:",Grosspay)
    print("Annual Income of employee is:",Grosspay*12)
elif(city=="B" and citytype==3):
    BasicPay=50000
    Grosspay=BasicPay + (0.1* BasicPay)+(0.5 *BasicPay)+7000+ 900-(200+(0.11*BasicPay) )
    print("Gross Pay of employee is:",Grosspay)
    print("Annual Income of employee is:",Grosspay*12)
elif(city=="C" and citytype==1):
    BasicPay=40000
    Grosspay=BasicPay + (0.3* BasicPay)+(0.5 *BasicPay)+6000+ 900-(200+(0.11*BasicPay) )
    print("Gross Pay of employee is:",Grosspay)
    print("Annual Income of employee is:",Grosspay*12)
elif(city=="C" and citytype==2):
    BasicPay=40000
    Grosspay=BasicPay + (0.2* BasicPay)+(0.5 *BasicPay)+6000+ 900-(200+(0.11*BasicPay) )
    print("Gross Pay of employee is:",Grosspay)
    print("Annual Income of employee is:",Grosspay*12)
elif(city=="C" and citytype==3):
    BasicPay=40000
    Grosspay=BasicPay + (0.1* BasicPay)+(0.5 *BasicPay)+6000+ 900-(200+(0.11*BasicPay) )
    print("Gross Pay of employee is:",Grosspay)
    print("Annual Income of employee is:",Grosspay*12)
elif(city=="D" and citytype==1):
    BasicPay=30000
    Grosspay=BasicPay + (0.3* BasicPay)+(0.5 *BasicPay)+5000+ 900-(200+(0.11*BasicPay) )
    print("Gross Pay of employee is:",Grosspay)
    print("Annual Income of employee is:",Grosspay*12)
elif(city=="D" and citytype==2):
    BasicPay=30000
    Grosspay=BasicPay + (0.2* BasicPay)+(0.5 *BasicPay)+5000+ 900-(200+(0.11*BasicPay) )
    print("Gross Pay of employee is:",Grosspay)
    print("Annual Income of employee is:",Grosspay*12)
elif(city=="D" and citytype==3):
    BasicPay=30000
    Grosspay=BasicPay + (0.1* BasicPay)+(0.5 *BasicPay)+5000+ 900-(200+(0.11*BasicPay) )
    print("Gross Pay of employee is:",Grosspay)
    print("Annual Income of employee is:",Grosspay*12)
elif(city=="E" and citytype==1):
    BasicPay=20000
    Grosspay=BasicPay + (0.3* BasicPay)+(0.5 *BasicPay)+4000+ 900-(200+(0.11*BasicPay) )
    print("Gross Pay of employee is:",Grosspay)
    print("Annual Income of employee is:",Grosspay*12)
elif(city=="E" and citytype==2):
    BasicPay=20000
    Grosspay=BasicPay + (0.2* BasicPay)+(0.5 *BasicPay)+4000+ 900-(200+(0.11*BasicPay) )
    print("Gross Pay of employee is:",Grosspay)
    print("Annual Income of employee is:",Grosspay*12)
elif(city=="E" and citytype==3):
    BasicPay=20000
    Grosspay=BasicPay + (0.1* BasicPay)+(0.5 *BasicPay)+4000+ 900-(200+(0.11*BasicPay) )
    print("Gross Pay of employee is:",Grosspay)
    print("Annual Income of employee is:",Grosspay*12)
elif(city=="F" and citytype==1):
    BasicPay=10000
    Grosspay=BasicPay + (0.3* BasicPay)+(0.5 *BasicPay)+3000+ 900-(200+(0.11*BasicPay) )
    print("Gross Pay of employee is:",Grosspay)
    print("Annual Income of employee is:",Grosspay*12)
elif(city=="F" and citytype==2):
    BasicPay=10000
    Grosspay=BasicPay + (0.2* BasicPay)+(0.5 *BasicPay)+3000+ 900-(200+(0.11*BasicPay) )
    print("Gross Pay of employee is:",Grosspay)
    print("Annual Income of employee is:",Grosspay*12)
elif(city=="F" and citytype==3):
    BasicPay=10000
    Grosspay=BasicPay + (0.1* BasicPay)+(0.5 *BasicPay)+3000+ 900-(200+(0.11*BasicPay) )
    print("Gross Pay of employee is:",Grosspay)
    print("Annual Income of employee is:",Grosspay*12)


tax = 0
if Grosspay*12 <= 250000:
    tax = 0
    print("tax",tax)
elif Grosspay*12 <= 500000:
    tax = (Grosspay*12 - 250000) * 0.05
    print("tax",tax)
elif Grosspay*12 <= 750000:
    tax = (Grosspay*12 - 500000) * 0.10 + 12500
    print("tax",tax)
elif Grosspay*12 <= 1000000:
    tax = (Grosspay*12 - 750000) * 0.15 + 37500
    print("tax",tax)
elif Grosspay*12 <= 1250000:
    tax = (Grosspay*12 - 1000000) * 0.20 + 75000
    print("tax",tax)
elif Grosspay*12 <= 1500000:
    tax = (Grosspay*12 - 1250000) * 0.25 + 125000
    print("tax",tax)
else:
    tax = (Grosspay*12 - 1500000) * 0.30 + 187500
    print("tax",tax)