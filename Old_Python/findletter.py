"""
input  : "i am going  to goa next month."
output  : first "o" index number is  :6
          second "o" index number is  :12
          third "o" index number is  :15
          fourth "o" index number is  :24

"""

s1="i am going to goa next month."

for i in range(len(s1)):
    if s1[i]=='o':
        print(i)