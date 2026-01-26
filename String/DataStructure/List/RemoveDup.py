l1 = ["red","yellow","green","blue"]

s1 = input("Enter Color You Want to remove : ")

if(s1 in l1):
    l1.remove(s1)
    print(s1,"is removed")
print(l1)