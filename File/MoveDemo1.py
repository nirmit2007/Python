import shutil
import os

fname = input("Enter File With Extension : ")

if os.path.exists(fname):
    shutil.move("Basic/Demo1.py","File/Demo2.py")
    print("Moved Successfully")
else:
    print("File Not Exist")