#Isabella Phung
#Period 2
#Project 7.2
#File: ch7_2.py
#This program checks if triangle is valid

def main():
    try:
        print("This program will check if a triangle is valid or not!")
        #gathering user input
        a,b,c= eval(input("Please enter in the three sides of the triangle, make sure each value is separated by a comma!  "))
        #testing when the triangle would not be valid
        if a+b< c:
            print("This triangle is not valid!")
        elif a+c< b:
            print("This triangle is not valid!")
        elif b+c<a:
            print("This triangle is not valid!")
        #prints out that triangle is valid if it passes all tests
        else:
            print("This tringle is valid!")

    #if user didn't type in all three numbers
    except NameError:
        print("You didn't enter in three numbers! Please try again!")
    #if user didn't type in numbers as values
    except TypeError:
        print("The inputs were not numbers! Please try again!")
    #if user didn't type in correct format
    except SyntaxError:
        print("Your input was not in the correct format. Please try again!")
    #when any unknown errors occur
    except:
        print("Oops! Something didn't work out! Please try again!")
main()
