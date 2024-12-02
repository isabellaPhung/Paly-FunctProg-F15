#Isabella Phung
#Period 2
#Project 7.5
#File: ch7_5.py
#This program calculates how much to pay Mr. Friedland after tutoring

def main():
    try:
        #gathers user input
        startHour, startMin = eval(input("Please enter in the start time in hours and minutes in military time separated by a comma instead of a colon: "))
        endHour, endMin = eval(input("Please enter in the end time in hours and minutes in military time separated by a a comma instead of a colon: "))

        #if it's past 7pm rate changes
        if endHour<= 19:
            rate=100
        else:
            rate= 150

        #finds hours
        hours= abs(endHour-startHour)

        #minute rate
        minRate= rate/60
        #minute total in money
        mintotal= minRate*abs(endMin+startMin)

        #total which is hour money total + minute money total
        total= hours*rate +mintotal
        #prints total
        print("The total is: $",total)

      #if user didn't type in all necessary numbers
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