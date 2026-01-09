no1 = int(input("Enter No1: "))
no2 = int(input("Enter No2: "))

'''hcf = 1

for i in range(1, no1 + 1):
    if no1 % i == 0 and no2 % i == 0:
        hcf = i

lcm = (no1 * no2) // hcf
print("LCM =", lcm)'''

max = no1 if no1 > no2 else no2
while True:
    if max % no1 == 0 and max % no2 == 0:
        lcm = max
        break
    max += 1
print("LCM =", lcm)