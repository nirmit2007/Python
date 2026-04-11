users = ["nirmit","vidhi","khushi"]

ans = filter(lambda x : len(x) > 5,users) # it will not give list
print(list(ans))