name = {"bob","rrr","anna","oppo","abcd"}

name = {i:"palindrome" if i == i[::-1] else "not plaindrome" for i in name}
print(name)