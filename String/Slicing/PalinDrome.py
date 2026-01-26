'''task 1
check string is palidrome or not using sllicing : naman  
'''

s1=input("Enter String : ")

if(s1 == s1[::-1]):
    print(s1,"is palinDrome")
else:
    print(s1,"is not palinDrome")
