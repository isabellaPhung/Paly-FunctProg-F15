#Isabella Phung
#Period 2
#Project 9.5
#File: ch9_5.py
#This program simulates a square dartboard

from random import *

def main():
    try:
        print("Hello, this is a square dartboard simulator!")
        darts= eval(input("Please input the amount of darts: "))
        odd=0
        for i in range(darts):
            x= randrange(1,101)
            if x<=62:
                odd=odd+1
        percentage= (100/darts)*odd
        print("The percentage the dart landed in an odd region is ", percentage, "%")
    except ZeroDivisionError:
        print("The dart did not land on any odd areas.")

main()
