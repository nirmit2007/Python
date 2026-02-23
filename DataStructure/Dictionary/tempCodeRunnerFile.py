data = {"Virat":[123,78,81],"rohit":[142,67,21]}

sum=0
totalScore =0
for i,j in data.items():
    print(f"{i}")
    for r in j:
        sum+=r
        print(r)
    print("total =",sum)
    totalScore+=sum
    sum=0

print("total score = ",totalScore)   