'''task  : 5 take list from user append all element in list and print pelindorme num in list 
 
         input : [121 , 131 , 123 ,145 , 789 ]
         output :  [121,131]'''

n = int(input("Enter the number of elements: "))
l1 = []

for i in range(n):
    ele = int(input("Enter the element: "))
    dup = ele
    palin = 0
    
    while ele > 0:
        temp = ele % 10
        palin = (palin * 10) + temp
        ele = ele // 10
    
    if dup == palin:
        l1.append(dup)

print(l1)
