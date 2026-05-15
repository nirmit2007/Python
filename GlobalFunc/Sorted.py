marks = {"ram":24,"shyam":20,"ganshyam":50,"soham":10}

result = sorted(marks.items(),key = lambda x:x[1],reverse=True)
print(result)


# nums = [5,2,-1,8,-20]

# #sort ignoring sign
# result = sorted(nums,key= lambda x:abs(x))
# print(result)