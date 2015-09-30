from random import randint

print("Time for Rock, Paper, Scissors. Write down your choice!")
print("Type 'help' to get an explanation of how the game works.")
userChoice = raw_input("")

if(userChoice == "help"):
    print("Simple explanation how to play RPS with lizard & spock added.")
    print("paper beats rock")
    print("scissors beats paper")
    print("rock beats lizard")
    print("lizard beats spock")
    print("spock beats scissors")
    print("scissors beats lizard")
    print("lizard beats paper")
    print("paper beats spock")
    print("spock beats rock")
    print("rock beats scissors")
    print("You can use the following options to make a choice:")
    print("For rock: r, R, rock or Rock")
    print("For scissors: sc, Sc, scissors or Scissors")
    print("For paper: p, P, paper or Paper")
    print("For scissors: l, L, lizard or Lizard")
    print("For scissors: sp, Sp, spock or Spock")
else:
    if(userChoice == 'r' or userChoice == 'R' or userChoice == 'Rock' or userChoice == 'rock'):
        choice = 1
    elif (choice == 'Sc' or choice == 'sc' or userChoice == 'scissors' or userChoice == 'Scissors'):
        choice =2
    elif (choice == 'P' or choice == 'p' or userChoice == 'Paper' or userChoice == 'paper'):
        choice = 3
    elif (choice == 'L' or choice == 'l' or userChoice == 'Lizard' or userChoice == 'lizard'):
        choice = 4
    elif (choice == 'Sp' or choice == 'sp' or userChoice == 'Spock' or userChoice == 'spock'):
        choice = 5
    else:
        print("That is not a valid choice");
        choice = 6

    randomChoice = (randint(1,5))
    if(randomChoice == 1):
        botsChoice = "Rock"
    elif(randomChoice == 2):
        botsChoice = "Paper"
    elif(randomChoice == 3):
        botsChoice = "Scissor"
    elif(randomChoice == 4):
        botsChoice = "Lizard"
    else:
        botsChoice = "Spock"
    print("Computers choice: " + botsChoice)
    if (randomChoice == choice):
        print("It's a draw!")
    elif (choice == 1 and randomChoice == 2) or (choice == 2 and randomChoice == 3) or (choice == 3 and randomChoice == 1) or (choice == 4 and randomChoice == 1) or (choice == 5 and randomChoice == 4) or (choice == 3 and randomChoice == 5) or (choice == 4 and randomChoice == 3) or (choice == 2 and randomChoice == 4) or (choice == 5 and randomChoice == 2) or (choice == 1 and randomChoice == 5):
        print("You lose!")
    else:
        print("You win! (tryhard)")