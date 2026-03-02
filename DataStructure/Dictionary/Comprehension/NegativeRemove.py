num = {"a":-1,"b":5,"c":-4}

final = {i:num[i] for i in num if num[i] > 0}
print(final)