# calc("+",10,20,30,40,50) but in - and / right to left

def calc(op, *nums):

    match op:

        case "+":
            result = 0
            for i in nums:
                result += i
            print("sum =", result)

        case "-":
            result = nums[-1]
            for i in reversed(nums[:-1]):
                result = i - result
            print("difference =", result)

        case "*":
            result = 1
            for i in nums:
                result *= i
            print("product =", result)

        case "/":
            result = nums[-1]
            for i in reversed(nums[:-1]):
                result = i / result
            print("quotient =", result)

        case _:
            print("Invalid operator")


calc("+", 10, 20, 30, 40, 50)
calc("-", 10, 20, 30, 40, 50)
calc("*", 10, 20, 30, 40, 50)
calc("/", 10, 20, 30, 40, 50)


