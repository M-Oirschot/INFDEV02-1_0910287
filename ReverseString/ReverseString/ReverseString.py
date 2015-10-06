print("Waiting on user input")
string = raw_input("")

#method 1
#output = string[::-1] #extended slices
#saw it was a mandatory to use a loop @ github (pretty late to update though)

#method 2
getLength = len(string)
char = getLength -1

i = 0
output = ""

while(i != getLength):
    output = output + string[char]
    char -= 1
    i += 1

print(output)