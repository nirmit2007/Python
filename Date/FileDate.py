import time

def show_time():
    print("Function called at :", time.ctime())

file = open("Date/log.txt", "a")

file.write("Function called at : " + time.ctime() + "\n")

file.close()

show_time()