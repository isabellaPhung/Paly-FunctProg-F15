#Isabella Phung
#Period 2
#Project 5.2
#File: ch5_2.py
#This program calculates grates

def main():
    print("Hello! This program will help calculate the letter grade of an exam score!")
    #collects user input
    x=eval(input("Please input an exam score:  "))
    #several if statements that check if the score is within a certain value
    #prints out letter grade based off of the standards of the if statement
    if x > 88:
        print("A")
    else:
        if x > 77:
            print("B")
        else:
            if x > 66:
                print("C")
            else:
                if x > 55:
                    print("D")
                else:
                    print("F")





main()