'''task :3 

ask user to enter the string  and store  in to the dict . 

input  :"mississiappi" 
output :{"m" :1 ,"i" :4,"s" :4 ,"p" :2, "a" :1}'''

a=input("Enter Name : ")
d1={}

for i in a:
    if i in d1:
        d1[i] = d1[i] + 1
    else:
        d1[i] = 1 
print(d1)

