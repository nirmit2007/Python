x = lambda n : "even" if n % 2 == 0 else "odd"
print(x(201))

x = lambda n1,n2 : "n1 is max" if n1>n2 else "n2 is max"
print(x(200,400))

x = lambda name : "palindrome" if name == name[::-1] else "not palindrome"
print(x("naman"))

