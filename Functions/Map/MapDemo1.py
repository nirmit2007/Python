sales = [1000,2000,3000,4000]

disc = map(lambda d : int(d-d*0.3),sales)
print(list(disc))