word = "machinelearning"

x = {i for i in word} # remove dup
print(x)

word = "pythonprogramming"

x = {i for i in word if i not in "aeiou"}
print(x)

names = ["Alice", "Bob", "Charlie", "David", "Alex"]

x ={i[0] for i in names}
print(x)