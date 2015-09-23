from random import randint
print("Time for Rock, Paper, Scissors. Write down your choice!")
print("Type 'help' to get an explanation of how the game works.")
userChoice = input("")

if(userChoice == "help"):
    print("Simple explanation how to play RPS")
    print("paper beats rock")
    print("rock beats scissors")
    print("scissors beats paper")
    print("You can use the following options to make a choice:")
    print("For rock: r, R, rock or Rock")
    print("For scissors: sc, Sc, scissors or Scissors")
    print("For paper: p, P, paper or Paper")
else:
    if(userChoice == 'r' or userChoice == 'R' or userChoice == 'Rock' or userChoice == 'rock'):
        choice = 1
    elif (choice == 'S' or choice == 's' or userChoice == 'scissors' or userChoice == 'Scissors'):
        choice =2
    elif (choice == 'P' or choice == 'p' or userChoice == 'Paper' or userChoice == 'paper'):
        choice = 3
    else:
        print("That is not a valid choice");
        choice = 4

    randomChoice = (randint(1,3)) # 1 = rock, 2 = paper, 3 = scissors
    if(randomChoice == 1):
        botsChoice = "Rock"
    elif(randomChoice == 2):
        botsChoice = "Paper"
    else:
        botsChoice = "Scissors"
    print("Computers choice: " + botsChoice)

    if (randomChoice == choice):
        print("It's a draw!")
    elif (choice == 1 and randomChoice == 2) or (choice == 2 and randomChoice == 3) or (choice == 3 and randomChoice == 1):
        rint("You lose!")
    else:
        print("You win! (tryhard)")