"""
task :1 

ask user to enter the  5 students name  and  marks  ans store in to the dict. 

ketan 90  aarav 89  harshil 88  shalin 99 purva 98 
output : {"ketan" :90 , "aarav" :89 , "harshil" :88 , "shalin" :99 , "purva" :98}
"""
d1={}
for i in range(4):
   name= str(input("Enter Name : "))
   marks= int(input("Enter Marks : "))
   d1[name] = marks
print(d1)   

temp = sorted(d1.values())
print(temp)
d2 = {}

for i in temp:
    for name,marks in d1.items():
        if marks == i:
            d2[name]=marks
print(d2)

'''task :3 

ask user to enter the string  and store  in to the dict . 

input  :"mississiappi" 
output :{"m" :1 ,"i" :4,"s" :4 ,"p" :2, "a" :1}
'''
