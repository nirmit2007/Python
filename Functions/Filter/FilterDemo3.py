names =["amit","neha","smruti","priya","ajna","amita","mayavati","sushila","radha","jay"]

ishow = map(lambda x : x.upper(),filter(lambda x : "i" in x,names))
print(list(ishow))