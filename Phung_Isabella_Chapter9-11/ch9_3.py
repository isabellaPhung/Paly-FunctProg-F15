#Isabella Phung
#Period 2
#Project 9.3
#File: ch9_3.py
#This program simulates a roulette

from random import *

def introGather(): #function to gather user input
    print("Hello! This program estimates estimates your chances with a roulette wheel,")
    spins=eval(input("Please enter the amount of spins: "))
    return spins

def main():
    red=0 #variable assignment
    black=0 #wins
    green=0
    redSpinTotal=0 #money total in end
    blackSpinTotal=0
    greenSpinTotal=0
    spins=introGather()
    for i in range(spins): #based off of the spins it generates different numbers and tests them
        x= randrange(1,38)
        if x <=18: #if red wins
            red=red+1
            redSpinMoney=2
            redSpinTotal=redSpinMoney+redSpinTotal
        elif x<=36: #if black wins
            black=black+1
            blackSpinMoney=2
            blackSpinTotal=blackSpinMoney+blackSpinTotal
        else: #if green wins
            green=green+1
            greenSpinMoney=35
            greenSpinTotal=greenSpinMoney+greenSpinTotal

        #bets subtracted
        redSpinTotal=redSpinTotal-1
        blackSpinTotal=blackSpinTotal-1
        greenSpinTotal=greenSpinTotal-1

    #prints all results
    print("Results:")
    print("Red: ", red)
    print("Black: ", black)
    print("Green: ", green)
    print("Total if you bet red every spin:", redSpinTotal, "dollars.")
    print("Total if you bet black every spin:", blackSpinTotal, "dollars.")
    print("Total if you bet green every spin:", greenSpinTotal, "dollars.")

main()