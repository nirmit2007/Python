data = {"Virat":[123,91,81],"Rohit":[142,67,21],"Hardik":[52,67]}

max = 0
for i,j in data.items():
    sum = 0
    for r in j:
        sum += r

    print(f"Total runs for {i}: {sum}")
    if sum > max:
        max = sum
print(f"Maximum total runs: {max}")