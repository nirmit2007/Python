def listPalin(l1):
    if l1 == l1[::-1]:
        return True
    return False


l1 = [121,122,123,122]
print(listPalin(l1))

def setCheck(s1):
    x = {i for i in s1 if len(i) > 4}
    return x

s1 = {"raj","parth","amit","sumit"}
print(setCheck(s1))

def dictFind(d1):
    x = {i:j for i,j in d1.items() if len(j) > 5}
    return x

d1 = {1:"nirmit",2:"khushi",3:"vidhi"}
print(dictFind(d1))