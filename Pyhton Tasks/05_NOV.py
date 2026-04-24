# E_arr=[]
# O_arr=[]
# while(True):
#     q = input("Enter number :")
#     if q == 'quit':
        
#         minimum = min(E_arr)
#         maximum = max(E_arr)
#         average = sum(E_arr) / len(E_arr)

#         print("even min =",minimum)
#         print("even max =",maximum)
#         print("even avg =",average)

#         minimum = min(O_arr)
#         maximum = max(O_arr)
#         average = sum(O_arr) / len(O_arr)

#         print("odd min =",minimum)
#         print("odd max =",maximum)
#         print("odd avg =",average)
#         break
#     else:
#         q = int(q)
#         if q % 2 == 0:
#             E_arr.append(q)
#         else:

#             O_arr.append(q)


# Disarium 
# harshad 

dis = []
har = []
for i in range(1,101):
    if i < 10 and i > 0:
        dis.append(i)
        har.append(i)
    
    elif i > 10 and i < 100 :
        j = i
        d1 = j// 10   # first digit
        d2 = j % 10    # second digit

        if d1 + (d2*d2) == i:
            dis.append(i)
        
        if i % (d1+d2) == 0:
            har.append(i)
    else:
        har.append(i)


print("Disarium : ", dis)
print("harshad  : ", har)

    
