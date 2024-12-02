#Isabella Phung
#Period 2
#Project 9.2
#File: ch9_2.py
#This program simulates a random walk

from random import *


def infoGather(): #gathers info
    print("Hello! This program simulates a random walk!")
    coinFlips= eval(input("Please enter in the amount of coin flips: "))
    return coinFlips



def randomRandom(coinFlips): #random number generator
    timesDone=[]
    for i in range(1000):
        placement=0
        for i in range(coinFlips):
            x= randrange(1,101)
            if x<=50:        #if heads
                placement=placement+1
            else:           #if tails
                placement=placement-1
        placement=abs(placement)
        timesDone.append(placement)
    return timesDone



def averageAverage(timesDone): #averages out the walks
    placementSum=0
    for j in (timesDone):
        placementSum=placementSum + j
    average= placementSum/ 1000
    return average



def main():
    coinFlips= infoGather()
    timesDone= randomRandom(coinFlips)
    average= averageAverage(timesDone)
    print("The average steps from the starting point is", average)
main()
