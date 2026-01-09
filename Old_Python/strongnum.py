# no=int(input("Enter No"))
# multy=1
# sum=0

# if no>0:  # 145 > 0
#    temp = no%10   # temp = 145 %10 =5 
   
# for i in range (1,temp+1):  # 5 ,1 
#     multy = multy*temp   # multy =5  
#     sum = sum + multy  
#     print(multy)
#     print(sum)  # 5 
# no = no//10  

# print(sum)
   
num =int(input("enter the  number  : "))
digit =len(str(num))
temp =num 
sum =0 
for i in range(digit):  # 2,3 
    r = temp %10    # temp = 1 %10 =1 
    fact =1 
    for j in range(1,r+1):
        fact = fact * j  # fact =1
    sum =sum +fact  # sum =145   
    temp = temp //10   # 0

if sum == num :  # 
    print("strong num")
