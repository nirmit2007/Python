'''Write a Python program that accepts a list of integers and calculates the length and the 
	fifth element. Return true if the 
	length of the list is 8 and the fifth element occurs thrice in the said list.
	Input:
	[19, 19, 15, 5, 5, 5, 1, 2]
	Output:
	True
	Input:
	[19, 15, 5, 7, 5, 5, 2]
	Output:
	False'''

n = int(input("Enter the number of elements: "))
l1 = []

for i in range(n):
    ele = int(input("Enter the element: "))
    l1.append(ele)

print(l1)
length = len(l1)

if(length==8):
    fifth_element = l1[4]
    if(l1.count(fifth_element)==3):
        print(True)
    else:
        print(False)
else:
    print(False)
