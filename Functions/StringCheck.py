def demo(**string):
    values = string.values()
    for i in values:
        if type(i) != str:
            return False
    return True

ans = demo(a="d",b="nirmit",c="b")
print(ans)