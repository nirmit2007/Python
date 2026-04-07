def test(a):
    print("Test function called")
    print(a)
    a()

def calling():
    print("Calling called")

test(calling)