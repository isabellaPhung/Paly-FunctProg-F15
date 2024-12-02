#Isabella Phung
#Period 2
#Project 9.1
#File: ch9_1.py
#This program estimates the value of pi by using a dartboard

from random import *

def introGather():
    print("Hello! This program estimates the value of pi by usuing a dartboard in a square cabinet,")
    print("and estimating based on the amount of darts that land and not land on the dartboard")
    dartNum=eval(input("Please enter the amount of darts: "))
    return dartNum

def randomRandom(dartNum):
    h=0
    for i in range(dartNum):
        x= 2*random()-1
        y= 2*random()-1
        if x**2 +y**2 <=1:
            h=h+1

    return h

def main():
    dartNum = introGather()
    h= randomRandom(dartNum)
    pi= 4*h/dartNum
    print("The estimated value of pi is", pi)

main()