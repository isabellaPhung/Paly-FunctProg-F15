#Isabella Phung
#Period 2
#Project 9.4
#File: ch9_4.py
#This program plays rock-paper-scissors-lizard-spock with you

from random import *

def randomHand():
    x = randrange(1,6)
    compHand=x
    return compHand

def versus(player, compHand):
    x=compHand
    if x == 1:     #scissors
        if player == "Rock" or player == "rock":
            return "Win", "Scissors2"
        elif player == "Paper" or player == "paper":
            return "Lose", "Scissors3"
        elif player == "Lizard" or player == "lizard":
            return "Lose", "Scissors4"
        elif player == "Spock" or player == "spock":
            return "Win", "Scissors5"
        else:
            return "Tie", "Scissors1"

    elif x == 2:    #paper
        if player == "Scissors" or player == "scissors":
            return "Win", "Paper1"
        elif player == "Rock" or player == "rock":
            return "Lose", "Paper2"
        elif player == "Lizard" or player == "lizard":
            return "Win", "Paper4"
        elif player == "Spock" or player == "spock":
            return "Lose", "Paper5"
        else:
            return "Tie", "Paper3"

    elif x == 3:    #rock
        if player == "Scissors" or player == "scissors":
            return "Lose", "Rock1"
        elif player == "Paper" or player == "paper":
            return "Win", "Rock3"
        elif player == "Spock" or player == "spock":
            return "Win", "Rock5"
        elif player == "Lizard" or player == "lizard":
            return "Lose", "Rock4"
        else:
            return "Tie", "Rock2"

    elif x == 4:    #lizard
        if player == "Scissors" or player == "scissors":
            return "Win", "Lizard1"
        elif player == "Rock" or player == "rock":
            return "Win", "Lizard2"
        elif player == "Paper" or player == "paper":
            return "Lose", "Lizard3"
        elif player == "Spock" or player == "spock":
            return "Lose", "Lizard5"
        else:
            return "Tie", "Lizard4"

    elif x == 5:   #spock
        if player == "Scissors" or player == "scissors":
            return "Lose", "Spock1"
        elif player == "Rock" or player == "rock":
            return "Lose", "Spock2"
        elif player == "Paper" or player == "paper":
            return "Win", "Spock3"
        elif player == "Lizard" or player == "lizard":
            return "Win", "Spock4"
        else:
            return "Tie", "Spock5"

    else:
        print(compHand)
        print("Something didn't work")


def main():
    print("Hello! This is a Rock-Paper-Scissors-Lizard-Spock simulator!")
    player= input("Please enter in your hand! (Press Enter to quit): ")
    gamesPlayed= 0
    userWins=0
    while player !="":
        compHandnum= randomHand()
        result, compHand=versus(player, compHandnum)
        gamesPlayed= gamesPlayed+1
        print("You: ", player)
        print("Computer: ", compHand)
        print("Results: ", result)
        if result == "Win":
            userWins=userWins+1
        player= input("Please enter in your hand! (Press Enter to quit): ")

    print("Games Played: ", gamesPlayed)
    print("User Wins:", userWins)


main()