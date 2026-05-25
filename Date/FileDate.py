import time

# FUNCTION
def show_time():
    print("Function called at :", time.ctime())


# WRITE TIME IN FILE
file = open("Date/log.txt", "a")

file.write("Function called at : " + time.ctime() + "\n")

file.close()


# FUNCTION CALL
show_time()