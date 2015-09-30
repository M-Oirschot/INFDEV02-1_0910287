import sys

print("Choose a figure to be drawn. \nType \n1 for a full square \n2 for a hollow square \n3 for Rectangle Triangle \n4 for isosceles triangle.")
userChoice = int(raw_input(""))

print("Choose a size")
size = int(raw_input(""))

if(userChoice == 1):
    i = 0
    t = 0
    endvar = ""
    while(t < size):
        while(i < size):
            endvar = endvar + "*"

            i = i + 1
        t = t + 1
        endvar = endvar + "\n"
        i = 0

     
sys.stdout.write(endvar + "\n")