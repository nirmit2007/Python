# n=int(input("enter the number :"))

# l1=[]
# for i in range(n):
#     element =int(input("enter the  element : "))
#     count = 0
#     no = element
#     for j in range(1,no+1):
#         if no % j == 0:
#             count += 1
#     if count == 2:    
#         print("count :",count)
#         l1.append(element)
# print(l1)




# l1 = [1,2,3,4,5,6,7,8,8,6,5,44,3,4,65,78,99,54,22,11,45]

# l2 = max(l1)
# l1.remove(l2)
# print(max(l1))



# n=int(input("enter the number :"))
# l1=[]
# for i in range(n):
#     ele =int(input("enter the  element : "))
#     palin=0 
#     temp=0
#     dup=ele   
#     for i in range (0,3):
#         if ele>0: 
#             temp = ele% 10
#             palin = (palin*10) + temp
#             ele = ele//10 
#     if(dup==palin):
#         l1.append(dup)
#     print(l1)



# l1= [19, 19, 15, 5, 3, 5, 5, 2]
# count2=0
# count1=0
# for i in (l1):
#     if i % 19 == 0:
#         count1+=1
#     elif i % 5 == 0:
#         count2+=1

# if count1 == 2 and count2 == 3:
#     print(True)
# else:
#     print(False)

'''
n=int(input("enter the number :"))
l1=[]
for i in range(n):
    ele =int(input("enter the  element : "))
    l1.append(ele)
#l1 = [19, 2, 15, 5, 2, 5, 1, 2]
#      1  2   3  4  5  6  7  8
print(l1)
count1=0
i5 = 0
length = len(l1)
if length == 8:
        for i in l1:
            i5 = l1[-4]
            if i == i5:
                count1+= 1 
        if count1 == 3:
            print(True)
        else: print(False)'''

'''
t1= 1,2,3,4,5,6,7,8,9,90
t2 = list(t1)
t2.append('shalin')
print(t2)
'''

'''
t1 = (10,20,30,[3,4,5],90)
t1[3][1] = "harshil"
print(t1)

'''

'''
l1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
l2 = []
for i in l1:
        j =list(i)
        j[2]= 100
        l2.append(tuple(j))
print(l2)
'''



# l1 = [[1,2,3],
#       [4,5,6],
#       [7,8,9]]
# l2 = []
# for i in range(len(l1)):
#     l3=[]
#     for j in range(len(l1[0])):
#         l3.append(l1[j][i])
#     l2.append(l3)
# # print(l2)

# for i in l2:
#     print(i)



# l1 = [[1,2,3],
#       [4,5,6],
#       [7,8,9]]
# for  i in range(len(l1)):
#     row1 = 0
#     for  j in range(len(l1)):
#         row1 +=  l1[i][j] 
#     print("Row sum = ",row1)

# for i in range (len(l1)):                    # 0 1 2
#     col1 = 0                    # cl 0
#     for  j in range(len(l1)):    # 0 1 2
#         col1 +=  l1[j][i]     #
#     print("column sum = ",col1)



'''
l1 = [[1,2], [3,5], [7,1]]
l2 = []
for i in range(3):   # i = [1,2]
    for  j in range(i+1,3):
        if l1[i][1] > l1[j][1]:
                temp = l1[i]
                l1[i] = l1[j]
                l1[j] = temp
print(l1)
'''


'''

result = {'Science': [88, 89, 62, 95, 50], 'Language': [77, 78, 84, 80, 60]}
Expected Output: [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
'''

'''

result = {'Science': [88, 89, 62, 95, 50], 'Language': [77, 78, 84, 80, 60]}
op = []
for i in range(5):
    op.append({'Science' : result['Science'][i], 'Language' : result['Language'][i]})

print(op)
'''

'''
d1 = {'c1': 'Red', 'c2': 'Green', 'c3': None}

new_dict = {}
for key, value in d1.items():
    if value is not None:
        new_dict[key] = value
print(new_dict)'''

'''

A Python Dictionary contains List as a value. Write a Python program to update the list values 
 in the said dictionary.
Original Dictionary:
{'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
Update the list values of the said dictionary:
{'Math': [89, 90, 91], 'Physics': [90, 92, 87], 'Chemistry': [90, 87, 93]}'''

o_d = {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
u_d = {}

for subject, marks in o_d.items():
    if subject == 'Math':
        u_d[subject] = [x + 1 for x in marks]
    elif subject == 'Physics':
        u_d[subject] = [x - 2 for x in marks]
    elif subject == 'Chemistry':
        u_d[subject] = marks[:]   

print("Original Dictionary:")
print(o_d)

print("Update the list values of the said dictionary:")
print(u_d)



'''
Dishant Shah
14:36
4.result = {'Science': [88, 89, 62, 95, 50], 'Language': [77, 78, 84, 80, 60]}
Expected Output: [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
task  :2 Write a Python program to drop empty items from a given dictionary.
Original Dictionary:
{'c1': 'Red', 'c2': 'Green', 'c3': None}
New Dictionary after dropping empty items:
{'c1': 'Red', 'c2': 'Green'}
Dishant Shah
14:49
Original list:
[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

Grouping a sequence of key-value pairs into a dictionary of lists:
{'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
task  :4A Python Dictionary contains List as a value. Write a Python program to update the list values 
 in the said dictionary.
Original Dictionary:
{'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
Update the list values of the said dictionary:
{'Math': [89, 90, 91], 'Physics': [90, 92, 87], 'Chemistry': [90, 87, 93]}'''