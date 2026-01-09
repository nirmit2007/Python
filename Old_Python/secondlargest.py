'''task : 2 Write a Python program to get the second largest number from a list.
	input  : [1,2,3,4,10,9,6,7]
	output : 9'''

l1=[1,2,3,4,10,9,6,7]

l2= max(l1)
l1.remove(l2)
print(max(l1))