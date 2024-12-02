#Isabella Phung
#Period 2
#Project 7.3
#File: ch7_3.py
#This program calculates calls in Lexington

def main():
    try:
        print("Hello! This program will calculate the cost of a call in Lexington!")
        #gathers user input
        minutes= input("Please enter in the length of the call in minutes:  ")
        #starting ammount for total
        total= 1.15
        #if statement that checks if minutes are above 2, if so, it will add 0.50 to every extra minute
        if minutes>2:
            tempMin= minutes-2
            for i in range(tempMin):
                total=total+0.5
            #prints total
            print("Your total is ${0:0.2f}". format(total))
        #if the given amount is 0, then this message is printed
        elif minutes<=0:
            print("You can't have less than or equal to 0 minutes in a call! Go call your aunt in Lexington and try again!")
        #if not, it simply prints the total
        else:
            print("Your total is $", total)

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
    except:
        print("Oops! Something didn't work out! Please try again!")

main()
