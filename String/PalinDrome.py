str=input("Enter String : ")
rev=""

for i in str:
    rev=rev+i 
if str==rev:
    print(str,"is PalinDrome")
else:
    print(str,"is Not PalinDrome")