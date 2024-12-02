#Isabella Phung
#Period 2
#Project 8.4
#File: ch8_4.py
#This program calculates how many ineffective workouts there are compared to effective workouts

def main():
    try:
        #variables assigned to starting values
        yes=0
        no=0
        #starts at one because day one is counted as a workout day
        totalDays=1
        print("Hello! This is a program that will track your workout progress! It will automatically end after 30 days, or will end when you tell it to!")
        #gathers user input
        days= input("How many days has it been since your last workout (press enter to end): ")

        #while loop that iterates as along as user types in something other than enter
        while days != "":
            days=eval(days)
            #checks if loop is greater than 3 or not
            if days>3:
                #when days is larger than 3, it adds one to no to count each time
                no=no+1

            elif days <= 3 and days >= 0:
                #when days is smaller than 3, it adds to yes to count each time
                yes=yes+1


            elif days < 0:
                #if user types in a negetive number, message given
                print("How did you go back in time bro? Try again please.")
                break

            #counter for total days
            totalDays=totalDays+days+1
            #if total days is larger or equal to 29 days, it will end
            #29 because day one is accounted for
            if totalDays >= 29:
                break
            #restarts loop
            days= input("How many days has it been since your last workout (press enter to end): ")

        #prints the amount of effective and ineffective workouts
        print(yes, "effective workouts and", no, "ineffective workouts")



    #if user didn't type in all three numbers
    except NameError:
        print("You didn't enter in the necessary numbers! Please try again!")
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
