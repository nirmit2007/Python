data = {"rohit":[100,20,121],"Virat":[90,98,78],"Kl":[151,89,7]}

# op:

# Score:

# Player Name : rohit
# Match 1:100
# Match 2:20
# Match 3:121

# toal : 241

# total score - 1000

for player, scores in data.items():
    filename = f"File/{player.lower()}.txt"  

    with open(filename, "a") as f:
        f.write(f"Player Name : {player}\n")

        total = 0
        match_no = 1

        for score in scores:
            f.write(f"Match {match_no} : {score}\n")
            total += score
            match_no += 1

        f.write(f"Total Score : {total}\n\n")

