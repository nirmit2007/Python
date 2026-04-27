dict = {"Nirmit":18,"Vidhi":20,"Khushi":23}

with open("File/DictShow.txt", "w") as f:
    for name, age in dict.items():
        f.write(f"name = {name}\n")
        f.write(f"age = {age}\n\n")
