no = int(input("Enter No: "))
original = no
sum_digits = 0
count = 0

temp = no
while temp > 0:
    count += 1
    temp = temp // 10

temp = no
while temp > 0:
    digit = temp % 10
    sum_digits += digit ** count
    temp = temp // 10

if sum_digits == original:
    print(original, "is an Armstrong number.")
else:
    print(original, "is not an Armstrong number.")