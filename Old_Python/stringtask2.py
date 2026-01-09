'''Write a python program that take one input string and in output count the no of words,
Find No of letters in String,Find the longest word in the String.
For Example:-
Input:-This is the python program
Output:-No of Words=5
	    No of letters=26(including whitespace)
	    Longest Word=program'''

s1=input("Enter String : ")

print(len(s1))
words = s1.split()
print("No of Words =", len(words))
print("No of letters =", len(s1))
print("Longest Word =", max(words,key=len))


