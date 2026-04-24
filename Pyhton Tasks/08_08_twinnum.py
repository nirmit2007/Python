# Write a python program that prompts the user to enter numbers and stops only when the use enter “QUIT” . After this 
# print sum  and average of the numbers, minimum and maximum number from given numbers entered by user.
#  Note: you are not allowed to use any built in structures like, list ,tuple etc. or any  builtin function like min, max  etc.
#  For 
#  Example:  Input:  4,1,5,”QUIT”
#  Output:
#  Sum=10
#  Average=3.333
#  Minimum number=1
#  Maximum number=5
 
'''
sum = 0
avg = 0
count = 0
min =None
max =None
while(1):
    num = input("Enter number :")
    if num != 'quit':
        num = int(num)
        sum += num
        count += 1
        if min == None or num < min:
            min = num
        if max == None or num > max:
            max = num

    else:
        break

avg = sum / count

print("sum = ",sum)
print("avg = ",avg)
print("min = ",min)
print("max = ",max)
'''


# Write a program that enters a single digit integer number and produces all possible 6-digit numbers for which the product 
# of their digits is equal to the entered number.
#  Example: "number" → 2
#  •111112 → 1 * 1 * 1 * 1 * 1 * 2 = 2
#  •111121 → 1 * 1 * 1 * 1 * 2 * 1 = 2
#  •111211 → 1 * 1 * 1 * 2 * 1 * 1 = 2
#  •112111 → 1 * 1 * 2 * 1 * 1 * 1 = 2
#  •121111 → 1 * 2 * 1 * 1 * 1 * 1 = 2
#  •211111 → 2 * 1 * 1 * 1 * 1 * 1 = 2
num = int(input("Enter number: "))

for i in range(100000, 1000000):
    product = 1
    temp = i
    while temp > 0:
        
        digit = temp % 10
        product *= digit
        temp //= 10
    if product == num:
        print(i)
