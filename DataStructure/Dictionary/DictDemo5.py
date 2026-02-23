data = {"Virat":[123,78,81],"rohit":[142,67,21]}

data.get("Virat")[1]=99
print(data)

data.update({"Hardik":[52,67]})
print(data)

for i,j in data.items():
    #print(f"{i} - {j}")
    print(f"{i}")
    for r in j:
        print(r)