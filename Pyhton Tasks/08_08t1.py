username = "shp"
password = "1234"

count = 0
for count in range (0,4):
 
    if(count != 0):
        A=input("Enter username(More than 8 characters) :")
        B=input("Enter password :")

        if(A == username and B == password):
           print("Login successful")
           print(count)
           break

        else:
            print("Try again")
            print(count)
        
print(count)
if(count == 4):
    print("Account locked")