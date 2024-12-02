#Isabella Phung
#Period 2
#Project 6.1
#File: ch6_1.py
#This program aligns string so last letter is in column 70 of display

def right_justify():
    print("Hello! This is a program that will align your text to the right in a certain way!")
    #gathers user input
    x= input("Please type in the word to be aligned!  ")
    #aligns it in a field of 70 minus the length of the string
    y= str.rjust(x, 70-len(x))
    #outputs value
    print(y)

right_justify()
