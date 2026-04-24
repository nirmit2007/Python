'''1 
1 2
1 2 3
1 2 3 4
1 2 3 4 5'''

'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
'''
#----------------------
'''
5 4 3 2 1 
5 4 3 2
5 4 3
5 4
5
'''
'''
for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()
    
'''
#--------------------------

'''
1 2 3 4 5 
2 3 4 5
3 4 5
4 5
5
'''
'''
for i in range(1,6):
    for j in range(i,6):
        print(j,end=" ")
    print()
    '''
#------------------------------------------

'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * *
  * * *
   * *
    *
'''
'''
for i  in range(1,5):
    for k in range(5,i,-1):
        print("",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i  in range(1,6):
    for k in range(1,i):
        print("",end=" ")
    for j in range(5,i-1,-1):
        print("*",end=" ")
    print()'''

#------------------------------------------------------
'''

for i in range(1,6):
    for j in range(1,6):
        if j == 1 or j == 5 or i == 1 or i==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

'''
#------------------------------------------------------

'''
i=1
while i==1:

    a=int(input("enter the  number  : "))
    b=int(input("enter the  number  : "))
    
    while True:
        print("1. addition")
        print("2. subtraction")
        print("3. multiplication")
        print("4. division")
        print("5. modulus")
        print("6. floor division")
        print("7. Exit")
        
        
        choice =int(input("enter the choice : "))
        match choice:
                case 1 :
                        print(a+b)
                        i=2
                case 2 :
                        print(a-b)
                        i=2
                case 3 :
                        print(a*b)
                        i=2
                case 4 :
                        print(a/b)
                        i=2
                case 5 :
                        print(a%b)
                        i=2
                case 6 :
                        print(a//b)
                        i=2
                case 7 :
                        print("Exit ")
                        break
                
                case _ :
                        print("invalid choice")

'''
#-----------------------------------------------------------------
sum = 0
while True:
    print("1. -> FRUITS")
    print("2. -> VEGETABLES")
    print("3. exit Shop")

    choice =int(input("enter the choice : "))
    match choice :
        case 1 :
            print("1.APPLE rs :100")
            print("2.KIWI rs :150")
            print("3.ORANGE rs :90")
            subchoice =int(input("enter the subchoice : "))
            match subchoice:
                case 1:
                    print("you selected apple ")
                    qty =int(input("enter the quantity : "))
                    sum +=100 * qty 
                    
                case 2 :
                    print("you selected kiwi ")
                    qty =int(input("enter the quantity : "))
                    sum += 150 * qty
                
                case 3 :
                    print("you selected orange ")
                    qty =int(input("enter the quantity : "))
                    sum += 90 * qty
                
        case 2:
            print("1.POTATOES rs :60")
            print("2.TOMATO rs :40")
            print("3.METHI rs :10")
            subchoice =int(input("enter the subchoice : "))
            match subchoice:
                case 1:
                    print("you selected potatoes ")
                    qty =int(input("enter the quantity : "))
                    sum += 60 * qty
               
                case 2 :
                    print("you selected tomato ")
                    qty =int(input("enter the quantity : "))
                    sum += 40 * qty
                
                case 3 :
                    print("you selected methi ")
                    qty =int(input("enter the quantity : "))
                    sum += 10 * qty
                
        case 3:
                
                break
        

print("Total bill is : ",sum)