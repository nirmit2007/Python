#------------------------------------------------------------------------------------------------------------------
'''[    LIST     ]'''

#task 1 :


# l1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# l2 = []

# for  i in range(len(l1)):
#     if i != 0 and i != 4 and i != 5:
#         l2.append(l1[i])
# print(l2)

# print(l1)



#------------------------------------------------------------------------------------------------------------------

'''' { Dict    }'''

#task 1 :

# n =int(input("Enter the number of elements you want in dict :"))
# d1={}
# No = []
# for i in range(n):
#     no = int(input("Enter the number you want to input :"))
#     No.append(no)

# for j in No:
    
#     d1[j]=j*j
# print(d1)
    
#------------------------------------------------------------------------------------------------------------------
#  task 2:

# data  = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# l1 = []
# for d in data:
#     for i in d.values():
#         if i not in l1:
#             l1.append(i)

# print(l1)


#------------------------------------------------------------------------------------------------------------------

'''    (     Tuple      )'''

# task 1 :

tuplex = ((2, "w"), (3, "r")) 
d1 = {}
for i,j in tuplex:
    d1[j] = i
print(d1)