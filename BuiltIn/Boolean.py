#Boolean

s1="python"

print(s1.startswith('p')) # checks whether string starts with given character
print(s1.endswith('m')) # checks whether string ends with given character
print(s1.isalpha()) # checks whether string contains only alphabets
print(s1.isnum()) # checks whether string contains only numbers
print(s1.isalnum()) # checks whether string contains only alphanumeric characters
#print(data.isdigit())
print("lower",s1.islower()) # checks whether string is in lowercase
print("upper",s1.isupper()) # checks whether string is in uppercase
print("isspace",s1.isspace())  # checks whether string contains only whitespace characters
print("is title",s1.istitle()) # checks whether string is in title case
print(s1.isprintable()) # checks whether string contains only printable characters
