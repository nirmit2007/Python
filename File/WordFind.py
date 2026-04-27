count=0
with open("File/demo1.txt","r") as f:
    for i in f.read():
        if i == " ":
            count+=1
print(count)


