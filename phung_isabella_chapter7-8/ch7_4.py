#Isabella Phung
#Period 2
#Project 7.4
#File: ch7_4.py
#This program calculates grades

def main():
    try:
        print("Hello! This program will help calculate the letter grade of an exam score!")
        #collects user input
        score =eval(input("Please input an exam score:  "))
        #several if statements that check if the score is within a certain value
        #prints out letter grade based off of the standards of the if statement
        score=round(score)
        if score >=88:
            print("A")
        elif score >=77:
            print("B")
        elif score >=66:
            print("C")
        elif score >=55:
            print("D")
        else:
            print("F")

    #if user didn't type in the correct numbers
    except NameError:
        print("You didn't enter in numbers! Please try again!")
    #if user didn't type in numbers as values
    except TypeError:
        print("The inputs were not in the correct format! Please try again!")
    #if user didn't type in correct format
    except SyntaxError:
        print("Your input was not in the correct format! Please try again!")
    #when any unknown errors occur
    #except:
        #print("Oops! Something didn't work out! Please try again!")


main()