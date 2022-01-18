# Rock paper scissors game
# rock -> kills scissors and is killed by paper
# paper -> kills rock and is killed by scissors
# scissors -> kills paper and is killed by rock

import random

options = ["Rock", "Paper", "Scissors"]
compWins = 0
userWins = 0
i = 0
j = 0
compRoundWins = 0
userRoundWins = 0
# IMPLEMENTATION OF THE THREE ROUNDS IN THE PROGRAM USING THE WHILE LOOP FOR VAR J******
while i < 3:
    compOption = random.choice(options)
    userOption = input("Input Rock(R), Paper(P) or Scissors(S)? : ")
    userOption.upper()
    if userOption is "R" and compOption is "Scissors":
        compWins = compWins + 1
        print("Comp wins!")
    elif userOption is "R" and compOption is "Paper":
        userWins = userWins + 1
        print("You win!")
    elif userOption is "R" and compOption is "Rock":
        print("Draw!")
    elif userOption is "P" and compOption is "Rock":
        userWins = userWins + 1
        print("You win!")
    elif userOption is "P" and compOption is "Scissors":
        compWins = compWins + 1
        print("Comp wins!")
    elif userOption is "P" and compOption is "Paper":
        print("Draw!")
    elif userOption is "S" and compOption is "Rock":
        compWins = compWins + 1
        print("Comp wins!")
    elif userOption is "S" and compOption is "Paper":
        userWins = userWins + 1
        print("You win!")
    elif userOption is "S" and compOption is "Scissors":
        print("Draw!")
    i = i + 1
    print("Comp score is : ", compWins * 100)
    print("Your score is : ", userWins * 100)
if compWins > userWins:
    print("COMP WINS THIS ROUND!")
    compRoundWins = compRoundWins + 1
else:
    print("YOU HAVE WON THIS ROUND!")
    userRoundWins = userRoundWins + 1
j = j + 1
