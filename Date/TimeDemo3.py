import time

print("start")
# time.sleep(3)
print("stop")

start = time.time() # ms from 1970 to till now
print(start)

for i in range(100000000):
    pass

end = time.time()
print(end-start)