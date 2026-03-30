def users(*names):  # return type is tuple
    print(names)

users() 
users("nirmit",25,[30])


#1st solution

# def students(x,*names):
#     print("names..",names)
#     print("x =",x)

#2nd solution 

def students(*names,x):
    print("names...",names)
    print("x = ",x)

students("nirmit","vidhi",x="khushi")