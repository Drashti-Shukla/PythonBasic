# Create a program that simulates a simple dice rolling game.
import random


def number():
    return random.randint(1,6)

def roll_dice():
    print("Welcome to Dice Rolling Game!")
    input("Press Enter to Roll the Dice!..")

    player1=number()
    compt=number()

    print("you Scored:",player1)
    print("Computer Scored",compt)
    msg = 'you win' if player1>compt else('you lose' if compt>player1 else 'Tie')
    return msg

print(roll_dice())