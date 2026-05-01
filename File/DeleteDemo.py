import os

# os.remove("File/demo1.txt")
# print("Deleted...")

if os.path.exists("File/demo2.txt"):
    os.remove("File/demo2.txt")
    print("file deleted")
else:
    print("file not found")