mumbai ={"raj","parth","amit","sumit"}
pune = {"jay","amit","kunal","neha"}
goa = {"rajvi","priya","amit","neha","krishna","raj"}

#find user who have attended all 3 events
#find user who is present in mumbai and goa
#find user who is present in pune and goa
#find user who is present in mumbai and goa but not in pune
#find user who is not presnt goa but mummbai and pune both

#1.find user who have attended all 3 events
a = mumbai.intersection(pune)
all = a.intersection(goa)
print(all)

#2.find user who is present in mumbai and goa
b = mumbai.union(goa)
print(b)

#3.find user who is present in pune and goa
c = pune & goa
print(c)

#4.find user who is present in mumbai and goa but not in pune
d = mumbai.intersection(goa)
e = d.difference(pune)
print(e)

#5.find user who is not presnt goa but mummbai and pune both
f = mumbai.intersection(pune)
g = f.difference(goa)
print(g)