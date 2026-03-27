#yesterday match score  get from gpt 
#find heighest wicket taker and heighest run scorer

runs = {("Samson",89), ("Ishan",54), ("Sky",47)}
wickets = {("Bumrah",4), ("Axar",3), ("Arshdeep",2)}

max_run = 0
run_player = ""

for p in runs:
    if p[1] > max_run:
        max_run = p[1]
        run_player = p[0]

max_wicket = 0
wicket_player = ""

for p in wickets:
    if p[1] > max_wicket:
        max_wicket = p[1]
        wicket_player = p[0]

print("Highest Run Scorer:", run_player, max_run)
print("Highest Wicket Taker:", wicket_player, max_wicket)