#Isabella Phung
#Period 2
#Project 7.4
#File: ch7_4.py
#This program calculates grades

def main():
    try:
        total=75
        Bags= eval(input("Please enter in the number of bags: "))
        total= total+ (Bags*10)
        if Bags >= 10:
            total= total+500
            print("The total fine is:", total)
        elif Bags<=0:
            print("You have no bags of litter! Great work!")
        else:
            print("The total fine is:", total)


    #if user didn't type in all three numbers
    except NameError:
        print("You didn't enter in numbers! Please try again!")
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
