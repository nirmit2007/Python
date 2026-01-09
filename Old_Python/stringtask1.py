'''ask user to enter the string and  first  and  last space with underscore (_). 
hint :  slicing +  replace

input : my name is harshil thakkar and i am master of table tennis.
output :my_name is harshil thakkar and i am master of table_tennis.'''

s1=input("Enter String : ")
s1=s1.replace(" ","_",1)[ : : -1].replace(" ","_",1)[ : :-1]
# s1=s1[::-1].replace(" ","_",1)[::-1]
print(s1)


