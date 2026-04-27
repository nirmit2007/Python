#file read..

# file = open("File/demo1.txt","r")
# x = file.read(5)
# print(x)

# with open("File/demo2.txt","r") as f:
#     x = f.readline()
#     print(x)

with open("File/Names.txt","r") as file:
    for i in file.readlines(): #[]
        print(i,end="")
