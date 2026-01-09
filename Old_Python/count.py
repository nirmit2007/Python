'''Write a Python program to find a list of integers with exactly two occurrences of nineteen
	 and at least three occurrences of five.  count 
	Return True otherwise False.
	Input:
	[19, 19, 15, 5, 3, 5, 5, 2]
	Output:
	True
	Input:
	[19, 15, 15, 5, 3, 3, 5, 2]
	Output:
	False'''
count1=0
count2=0
for i in range(8):
    ele = int(input("Enter the element: "))
    if ele==19:
        count1+=1   
    elif ele==5:
        count2+=1

if count1==2 and count2==3:
    print("True")
else:
    print("False")     
       