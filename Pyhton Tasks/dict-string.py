# d1={}

# for i in range(5):
#     name = input("Enter name of student :")
#     marks = int(input("Enter marks of student :"))
#     d1[name] = marks

# temp = sorted(d1.items())
# print(temp)
'''
string = input("Enter the string :")
d1 = {}
size = len(string)

for i in string:
    count = 0
    for j in string:   
        if j == i:
            count += 1
    d1[i] = count     

print(d1)'''

'''
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200} 
d1.update(d2) 
print(d1)'''

# myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# myDict.pop('a')
# print(myDict)


'''

string = "Shalin Hareshkumar Patel"
s1=(string[0])
s2=(string[7])
s3 =(string[19:])
print(f"{s1}.{s2}.{s3}")
'''
'''
s1 = input("Enter first string :")
s2 = input("Enter second string :")

e1 = s1[0:3] + s2[3 :]
e2 = s2[0:3] + s1[3 :]

print(e1)
print(e2)
'''


"""
Original dictionary: sort by value asc to desc 

d1 = {'name1': 'Theodore', 'name2': 'Mathew', 'name4': 'Roxanne', 'name3': 'David'}
output : {'name3': 'David', 'name2': 'Mathew', 'name4': 'Roxanne','name1': 'Theodore'}
"""

# d1 = {'name1': 'Theodore', 'name2': 'Mathew', 'name4': 'Roxanne', 'name3': 'David'}
# d2={}
# l1 = list(d1.values())

# for i in range(len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[i]>l1[j]:
#             l1[i], l1[j] = l1[j],l1[i]

# for l in l1:
#     for key in d1:
#         if d1[key] == l and key not in d2:
#             d2[key]=l

# print(d1)





"""
Original dictionary: sort by value asc to desc 

d1 = {'name1': 'Theodore', 'name2': 'Mathew', 'name4': 'Roxanne', 'name3': 'David'}
output : {'name3': 'David', 'name2': 'Mathew', 'name4': 'Roxanne','name1': 'Theodore'}
"""



'''

d1 = {'name1': 'Theodore', 'name2': 'Mathew', 'name4': 'Roxanne', 'name3': 'David'}
d2={}
li = list(d1.values())

for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i] > li[j]:
            li[i], li[j] = li[j],li[i]

for l in li:
    for key in d1:
        if d1[key]==l and key not in d2:
            d2[key]=l
print(d2)'''



# s1 = "I am going to goa next month."

# print("index of first o is :",s1.index("o"))
# print("index of second o is :",s1.index("o",7))
# print("index of third o is :",s1.index("o",13))
# print("index of forth o is :",s1.index("o",16))
'''
for i in range(len(s1)):
   if s1[i] == "o":
        print(i) '''


'''
Task 2 :

s1 = "restart"
s2 = s1[0]
s1 = s1.replace("r","@")
print(f"{s2}{s1[1:]}")'''

'''
s1 = "my name is gabru"
#s1 = input("Enter string : ")
s1 = s1.replace(" ","_",1)
print(s1)
s2 = s1[8:]
s2 = s2.replace(" ","_")
print(f"{s1[0:8]}{s2}")'''
'''

s1 = input("Enter string : ")
print(s1.replace(" ","_",1)[::-1].replace(" ","_",1)[::-1])
print(s1.split("e",1))
print(s1.rsplit("s",2))

'''

#-------------------------------------------------   29 - AUG - 25 -----------------------------------------
'''

task  :4 take list from user append all element in list and print pelindorme word in list  
         input : ["java", "python", "php","cpp","flutter","maam"]
         output :  ['php','maam']'''


# n = int(input("Enter the no for no of elements you want to add in list : "))
# l1=[]

# for i in range(n):
#     a=input("Enter string / character :")
#     l1.append(a)

# for i  in l1:
#     if i == i[::-1]:
#         print(i)

'''task  :2 take list from user append all element in list and print longest word in list  
         input : ["java", "python", "php","cpp","flutter"]
         output :  flutter'''


# n = int(input("Enter the no for no of elements you want to add in list : "))
# l1=[]
# l2=[]
# for i in range(n):
#    a=input("Enter string / character :")
#    l1.append(a)


# for i in range(len(l1)):
#     count = 0
#     for j in range(i+1,len(l1)):
#         if len(l1[i]) < len(l1[j]) :
#             l2.append(l1[j])

# print(l2[-1])
'''
Write a Python program to find the length of a given list of non-empty strings.
	Input:
	['cat', 'car', 'fear', 'center']
	Output:
	[3, 3, 4, 6]
	Input:
	['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
	Output:
	[3, 3, 7, 5, 2, 4, 0]'''


# n = int(input("Enter the no for no of elements you want to add in list : "))
# l1=[]
# l2=[]
# for i in range(n):
#     a=input("Enter string / character :")
#     l1.append(a)
# size=0
# for i in l1:
#     size = len(i)
#     l2.append(size)

# print(l2)

'''
Write a Python program to count the number of strings from a given list of strings. 
	The string length is 2 or more and the first and last characters are the same.
	
	Sample List : ['abc', 'xyz', 'aba', '1221']
	Expected Result : 2
rmp-penf-trd'''


# l1 = ['abc', 'xyz', 'aba', '1221']
# count = 0
# for i in l1:
#     if len(i) >= 2:
#         if i[0] == i[-1]:
#             count+=1
        
# print(count)




'''task:7 
Write a Python program to find strings in a given list containing a given substring.
Input:
[(ca,('cat', 'car', 'fear', 'center'))]
Output:
['cat', 'car']
Input:
[(o,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
Output:
['dog', 'donut', 'todo']'''
'''

l1 = [(('cat', 'car', 'fear', 'center'))]
s ='ca'
l3 = []

for i in l1[0]:
    if s in i:
        l3.append(i)
print(l3)
'''



'''
Original list:
[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

Grouping a sequence of key-value pairs into a dictionary of lists:
{'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}'''

'''
d1 = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d2 = {} 
for key, value in d1:
    if key not in d2:
        d2[key] = [value]     
    else:
        d2[key].append(value)
    
print(d2)


'''

'''
Write a Python program to  a dictionary based on values.
Original Dictionary:
{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
Marks greater than 170:
{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
'''
'''
d1 = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
d2 = {} 
for key,value in d1.items():
    if value > 170:
        d2[key] = value

print(d2)'''


#task  :3 Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''
l1 = [(2,5), (1,2), (4,4), (2,3), (2,1)]
n = len(l1)
for i in range(n):
    for  j in range(0, n-i-1):
            if l1[j][-1] > l1[i][-1]:
                l1[j], l1[j+1] = l1[j+1], l1[j]

print(l1)'''


sample = ['p','q']
n = int(input("Enter you want to no of pairs :"))
result = [] 

for i in range(1,n+1):
    for it in sample:
        result.append(it + str(i))

print(result)