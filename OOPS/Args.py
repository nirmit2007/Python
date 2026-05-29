""" create class function it will accept args as argument passes only number check it.if all are numbers return sum of all numbers and print it """

class Demo:
    def add(self, *args):
        print("Sum =", sum(args))

obj = Demo()

n = int(input("How many numbers? "))

nums = []

for i in range(n):
    nums.append(int(input("Enter number: ")))

obj.add(*nums)