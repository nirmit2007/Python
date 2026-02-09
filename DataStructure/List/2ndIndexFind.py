marks = [90,40,45,60,90,40,45]

x = int(input("Enter marks to find index: "))
count = 0
for i in range(len(marks)):
    if marks[i] == x:
        count += 1
        if count == 2:
            print(i)
            break
