'''Write a C program to input electricity unit charges and calculate total electricity bill according to the given condition:
For first 50 units Rs. 0.50/unit
For next 100 units Rs. 0.75/unit
For next 100 units Rs. 1.20/unit
For unit above 250 Rs. 1.50/unit
An additional surcharge of 20% is added to the bill'''


unit = int(input("Enter Units"))

if unit>=0 and unit<=50:
    bill = unit*0.5
    surcharge = unit*.2
    total_charge = bill + surcharge
    print("Total Bill = ",total_charge)

elif unit>=51 and unit<=150:
    bill = 50*0.50 + (unit - 50)*0.75
    surcharge = unit*.2
    total_charge = bill + surcharge
    print("Total Bill = ",total_charge)

elif unit>=151 and unit<=250:
    bill = 100*0.75 + (unit - 150)*1.20
    surcharge = unit*.20
    total_charge = bill + surcharge
    print("Total Bill = ",total_charge)

elif unit>=251 and unit<=250:
    bill = 100*1.2 + (unit - 150)*1.50
    surcharge = unit*.20
    total_charge = bill + surcharge   
    print("Total Bill = ",total_charge)

elif unit>=251:
    bill = 220 + (unit - 250)*1.50
    surcharge = unit*.20
    total_charge = bill + surcharge   
    print("Total Bill = ",total_charge)    