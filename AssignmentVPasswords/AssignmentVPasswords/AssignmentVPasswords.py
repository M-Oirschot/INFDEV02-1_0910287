import re
while True:
    print("Enter a password")
    pw = input("")

    status = 0

    if(len(pw) <= 7):
        print("test") #let status be 0
    elif(len(pw) >= 8 and len(pw) <= 15):
         status = status+2
         print("pw is longer then 8 and shorter or equal then 15")
    elif(len(pw) >= 16):
        status = status+4
        print("longer or equal to 16")

    if re.search(r'\d', pw):
        print ("Has a digit")
        status = status+1
    if re.search(r'[A-Z]', pw):
        status = status+1
    if re.search(r'[a-z]', pw):
        print ("Has lowercase letter")
        status = status+1
    if re.search(r'[~!@#$%^&*()_+{}":;\']', pw):
        print ("Has a special character")
        status = status+1

    def wordcount(value):
        # Find all non-whitespace patterns.
        list = re.findall("(\S+)", value)
        # Return length of resulting list.
        return len(list)

    amountOfWords = wordcount(pw)
    if(amountOfWords >= 3):
        status = status+10

    if(status <= 4):
        print("Password strength: Weak")
    elif(status > 5 and status <= 13):
        print("Password strength: Medium")
    elif(status > 14):
        print("Password strength: Strong")

    print(status)