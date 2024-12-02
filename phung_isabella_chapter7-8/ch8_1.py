    #Isabella Phung
#Period 2
#Project 8.1
#File: ch8_1.py
#This program finds nth term of a sequence


def main():
    try:
        print("This program will find the nth term of a sequence!")
        #gathers user input and assigns to n
        n= input("Please enter in the nth term of the sequence, press enter to end the program: ")

        #while loop that ends when user types space
        while n != "":
            #starting numbers
            num1=1
            num2=2
            nxtNum=0
            #evaluates
            n=eval(n)
            #to compensate for the assigned variables num1 and num2
            n=n-2
            #for loop that will multiply based off of how long n is
            for i in range(n):
                nxtNum=num1*num2
                num1=num2
                num2=nxtNum
            #prints out results
            print("The", n,"term of this sequence is:", nxtNum)
            n= input("Please enter in the nth term of the sequence, press enter to end the sequence: ")
        #message when exited
        print("Program exited.")


    #if user didn't type in the necessary numbers
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