#fileobject = open("location | path ","mode")

#if file present at given path it will overwrite
#if file is not present at given path it will create and write data

name = "Nirmit"
file = open("File/demo1.txt","w")
file.write(f"\nMy Name is {name}")
file.close()

# file  = open("demo1.txt","w")
# #file.write(f"Hi this is  {name}")
# print(f"hi this is {name}",file=file)
# file.close()
#file.write("ok") error..



