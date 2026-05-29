class Demo:
    def sum(self, no1, no2):
        return no1 + no2

obj = Demo()

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", obj.sum(a, b)) 