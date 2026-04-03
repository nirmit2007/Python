def data(**mydata):
    print("kwrgs...",mydata) # stores in dict

data(name="nirmit",age=18,collage="newlj")

def demo(x,**kwargs):
    print("x...",x)
    print("kwargs...",kwargs)

demo(x=16,age=18)
