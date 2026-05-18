""" l1 = [10,-20,30,-40,50]
print(min(l1,key=abs))
print(max(l1))

names = ["raj","parth","amitabh"]
print(min(names,key=len))
print(max(names,key=len))

lt = [("sam",80),("raj",90)]

print(min(lt,key=lambda x:x[1]))
print(max(lt,key=lambda x:x[1]))

nums = [-5,2,-1,1,7]

print(min(nums,key=lambda x: abs(x)))

str = "jay","abcd","abcde","abcdef"

print(max(str,key=lambda x :len(x) if len(x) % 2 == 0 else 0)) """

""" l1 = [10,-20,30,-40,50]

ans = sum(i for i in l1 if i%2 == 0)
print(ans) """

""" l1 = [1,2,3,4]

ans = sum(i*i for i in l1)
print(ans) """

""" str = "jay"

vowel = sum(i in "aeiou" for i in str)
print(vowel) """

""" num = 1234
digitsum = sum(int(i) for i in str(num))
print(digitsum) """

num = 1234
evensum = sum(int(i) for i in str(num) if int(i)%2==0)
print(evensum)
