str = input("Enter string :")
for i in range (len(str)):
    if(str[i] == 'a' or str[i] == 'e' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u'):
        with open("vovel_chars.txt","a") as file1:
            file1.write(f"{str[i]}")
    else:
        with open("constant_chars.txt","a") as file:
            file.write(f"{str[i]}")

