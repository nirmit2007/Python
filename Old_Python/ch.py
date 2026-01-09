ch=str(input("Enter Ch :"))

if ch>='A' and ch<='Z':
    ch = ord(ch) + 32  # ord = ordinal : convert into ASCII value
    print("Lower Case : ",chr(ch))  # chr = character : convert into ch value
else:
    ch = ord(ch) - 32  
    print("Upper Case : ",chr(ch)) 
        