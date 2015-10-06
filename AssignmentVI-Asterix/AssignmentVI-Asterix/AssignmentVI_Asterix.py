import sys

print("Choose a figure to be drawn. \nType \n1 for a full square \n2 for a hollow square \n3 for Rectangle Triangle \n4 for isosceles triangle.")
userChoice = int(raw_input(""))

print("Choose a size")
size = int(raw_input(""))

if(userChoice == 1):
    endvar = ""
    for i in range(size):
        for j in range(size):
            endvar += "*"
        endvar += "\n"

    # This does the same but then with only 1 forloop
    #endvar = ""
    #lineCounter = 0
    #while lineCounter != size:
    #    for i in range(size):
    #        endvar += "*"
    #    endvar += "\n"
    #    lineCounter += 1

if(userChoice == 2):
    endvar = ""

if(userChoice == 3):
    endvar = ""
    lineCounter = 0
    cnt = int(1)
    while lineCounter != size:
        for i in range(cnt):
            endvar += "*"
        cnt += 1
        endvar += "\n"
        lineCounter += 1
        
sys.stdout.write(endvar + "\n")