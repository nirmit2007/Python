no=int(input("Enter No of 3 digit : "))
temp=0
cube=0
swap=no

while(no>0):
    temp = no % 10 #3
    cube = temp * temp * temp + cube # 27
    no = no // 10  #12

no=swap
if(cube==swap):
    print(cube,"is armstrong number.")