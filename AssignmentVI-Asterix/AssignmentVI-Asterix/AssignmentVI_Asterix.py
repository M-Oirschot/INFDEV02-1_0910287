import sys
while True:
    print("Choose a figure to be drawn. \nType \n1 for a full square \n2 for a hollow square \n3 for Rectangle Triangle \n4 for isosceles triangle.\n5 for a circle")
    userChoice = int(raw_input(""))

    print("Choose a size")
    size = int(raw_input(""))

    if(userChoice == 5):
        import math

    endvar = ""
    cnt = 0

    if(userChoice == 1): 
        for i in range(size):
            for j in range(size):
                endvar += "*"
            endvar += "\n"

        #lineCounter = 0
        #while lineCounter != size:
        #    for i in range(size):
        #       endvar += "*"
        #    endvar += "\n"
        #    lineCounter += 1

    elif(userChoice == 2):
        length = size-1
        for i in range(size):
            for j in range(size):
                if(i == 0 or j == 0):
                    endvar += "*"
                elif(i == length or j == length):
                    endvar += "*"
                else:
                    endvar += " "
            endvar += "\n"

    elif(userChoice == 3):
        lineCounter = 0
        cnt = 1 
        while (lineCounter != size):
            for i in range(cnt):
                endvar += "*"
            cnt += 1
            endvar += "\n"
            lineCounter += 1

    elif(userChoice == 4):
        cnt = 1
        for i in range(size):
            spaces = size - i
            for x in range(spaces):
                endvar += " "
            for y in range(cnt):
                endvar += "*"
            endvar += "\n"
            cnt += 2

    elif(userChoice == 5):
        for y in range(-size, size + 1):
            for x in range(-size, size + 1):
                if math.sqrt((y**2)+(x**2)) <= size + 0.2:
                    endvar += "*"
                else:
                    endvar += " "
            endvar += "\n"

    sys.stdout.write(endvar + "\n")