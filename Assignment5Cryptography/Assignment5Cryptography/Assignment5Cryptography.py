import re
import sys

print("Input a string")
string = input("")
print("Input number")
shift = int(input(""))

length = len(string)
i = 0

while i != length:
    curChar = int(ord(string[i]))
    if re.search(r'[A-Z]', string[i]):
        changeChar = curChar + shift
        while changeChar >= 91:
            difference = changeChar - 90
            changeChar = 64 + difference

    elif re.search(r'[a-z]', string[i]):
        changeChar = curChar + shift
        while changeChar >= 123:
            difference = changeChar - 122
            changeChar = 96 + difference

    sys.stdout.write(chr(changeChar))
    i = i + 1
sys.stdout.write("\n")
