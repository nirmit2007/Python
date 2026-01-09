str=input("Enter String : ")
count=0

'''for i in range(len(str)):
    if(str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u'):
       count+=1

print("Count Of Vowels = ",count)'''

for i in str:
    if i in 'aeiouAEIOU':
        count+=1
print("Count Of Vowels = ",count)