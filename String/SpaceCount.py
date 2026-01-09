str=input("Enter String : ")
count=0

for i in range(len(str)):
    if(str[i]==' '):
        count+=1

print("Count Of Space = ",count)