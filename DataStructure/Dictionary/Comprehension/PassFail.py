marks = {"nirmit" : 45,"khushi" : 66,"vidhi" : 100}

result = {i:"pass" if marks[i] > 60 else "fail"for i in marks}
print(result)