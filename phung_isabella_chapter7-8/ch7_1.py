#Isabella Phung
#Period 2
#Project 7.4
#File: ch7_4.py
#This program checks if trangle is a right triangle or not

def main():
    try:
        print("This program will check if a triangle is right or not!")
        #gathers user input
        a,b,c= eval(input("Please enter in the sides of the triangle, with each value separated by a comma:  "))
        #checks if any of the values are negetive
        if a<0:
            print("You entered in a negetive number! Please try again with positive numbers!")
        elif b<0:
            print("You entered in a negetive number! Please try again with positive numbers!")
        elif c<0:
            print("You entered in a negetive number! Please try again with positive numbers!")
        else:
            #checks using Pythagorean theorum to see if triangle is right
            if a**2+b**2==c**2:
                print("This trangle is a right trangle!")
            #if the values don't pass the Pythagorean theorum, it is not a right triangle
            else:
                print("This triangle is not a right triangle!")
    #if user didn't type in all three numbers
    except NameError:
        print("You didn't enter in three numbers! Please try again!")
    #if user didn't type in numbers as values
    except TypeError:
        print("The inputs were not numbers! Please try again!")
    #if user didn't type in correct format
    except SyntaxError:
        print("Your input was not in the correct format. Please try again!")
    #when an unknown error occurs
    except:
        print("Oops! Something didn't work out! Please try again!")
main()
