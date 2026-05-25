from datetime import time as t
from datetime import datetime
samay=t(17,17,17)
print(samay)
print(samay.minute)
print(samay.second)
print(samay.hour)

#timestamp
now = datetime.now()
print(now.timestamp()) #1970 1st january

dt = datetime.fromtimestamp(0) #1ms pass
print(dt)

dtnow = datetime.fromtimestamp(now.timestamp())
print(dtnow)

#ctime
print(now.ctime())
#isofomrmate
print(now.isoformat())

#replace
new_date = now.replace(year=2050,month=5,day=20)
print(new_date)