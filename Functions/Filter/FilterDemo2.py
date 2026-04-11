names =["amit","neha","smruti","priya","ajna","amita","mayavati","sushila","radha","jay"]

endsWITHa = map(lambda x : x.upper(),filter(lambda x : x.endswith('a'),names))
print(list(endsWITHa))

