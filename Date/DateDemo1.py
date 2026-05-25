# import datetime
# import time
# import calendar

from datetime import date
today = date.today()
print(today)
print(type(today))

# accessing year month day

print(today.day)
print(today.month)
print(today.year)
print(today.weekday()) # it starts with 0 index of day
print(today.isoweekday()) # it starts with 1 index of day


#custumised date

d1 = date(2026,5,31) # onlt this format allows & also not 05 only 5 (decimal 0 is not allowed)
print(d1)