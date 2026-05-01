import shutil
import os

filename = input("Enter File Name : ")

if os.path.exists(filename):
    shutil.copy2("py.txt","File/python.txt")
    print("File Copied and Pasted...")
else:
    print("File Not Exists")