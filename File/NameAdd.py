with open("File/Names.txt", "a") as f:
    while True:
        name = input("Enter Names : ").strip()
        if name.lower() == "exit":
            break
        f.write(name + "\n")