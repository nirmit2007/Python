name="java"
chr=input("Enter Character of name that you want to search : ")
index=0

for i in name:
    if(i==chr):
        print("Character found at index :",index)
        break
    index+=1
        