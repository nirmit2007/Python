name=input("Enter Name : ")

#lwr to upr
'''for i in name:
    print(chr(ord(i)-32),end='')'''

#upr to lwr
for i in name:
    if(ord(i)<=97 and ord(i)>=121):
        print(chr(ord(i)+32),end='')
    else:
        print(i,end='')


