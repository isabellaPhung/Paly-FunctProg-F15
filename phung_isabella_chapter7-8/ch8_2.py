#Isabella Phung
#Period 2
#Project 8.4
#File: ch8_4.py
#This program calculates the missing variable of a physics equation
#the values might be incorrect because there wasn't an example problem I could use

import math

#method for solving for time
def timesolver(s,v,h):
    #minus verision of the quadratic equation
    t1=((v+s)-math.sqrt(((v+s)**2)-(4*4.9*(-h))))/2*(4.9)
    #plus version of quadratic equation
    t2=((v+s)+math.sqrt(((v+s)**2)-(4*4.9*(-h))))/(2*(4.9))
    print(t1)
    print(t2)
    return t1, t2

def main():
    #try:
        print("Hello, this will calculate the missing variable in a physics equation! Please be mindful of units!")
        print("Also please enter in the variables in order from s, time, velocity, height.")
        #gathers user input
        x= input("Please enter in the first value (press enter to end): ")

        #while loop that iterates as along as user types in something other than enter
        while x != "":
            #gathers more user input
            isIt1= input("Which variable was x (s, time, velocity, or height): ")
            y= eval(input("Please enter in the second value: "))
            isIt2= input("Which variable was y (s, time, velocity, or height): ")
            z= eval(input("Please enter in the third value: "))
            isIt3= input("Which variable was z (s, time, velocity, or height): ")
            #evaluates because x had to be compared in the while loop
            x=eval(x)

            #value assignment for gravity
            g=9.8

            #if x is time, or velocity, or height, it will assign the x value to a variable
            if isIt1 == "time":
                t=x
            elif isIt1 == "velocity":
                v=x
            elif isIt1 == "height":
                h=x
            elif isIt1 == "s":
                s=x

            #if y is time, or velocity, or height, it will assign the x value to a variable
            if isIt2 == "time":
                t=y
            elif isIt2 == "velocity":
                v=y
            elif isIt2 == "height":
                h=y
            elif isIt1 == "s":
                s=y

            #if z is time, or velocity, or height, it will assign the x value to a variable
            if isIt3 == "time":
                t=z
            elif isIt3 == "velocity":
                v=z
            elif isIt3 == "height":
                h=z
            elif isIt1 == "s":
                s=z

            #if loop that checks for what the missing variable is
            if isIt1 != "s" and isIt2 != "s" and isIt3 != "s":
                #rearranged formula
                s=(-0.5*g*t**2+v*t+h)/t
                #prints value
                print("S is: ", s)

            elif isIt1 != "time" and isIt2 != "time" and isIt3 != "time":
                #plugs variables into time equation
                t1, t2= timesolver(s,v,h)
                #if loop that decides which answer to return
                if t1 <= 0:
                    print("The time is:",t2)
                elif t2 <= 0:
                    print("The time is:",t1)
                elif t1 <= 0 and t2 <= 0:
                    print("The time is:", t1, "and", t2, ". Both ended up with either 0 or a negetive value.")
                elif t1 > 0 and t2 > 0:
                    print("The two times recieved were ", t1, "and", t2)

            elif isIt1 != "velocity" and isIt2 != "velocity" and isIt3 != "velocity":
                #rearranged formula
                v=(s*t-h+0.5*g*t**2)/t
                #prints value
                print("The velocity is: ", v)

            elif isIt1 != "height" and isIt2 != "height" and isIt3!= "height":
                #rearranged formula
                h=s*t+0.5*g*t**2-v*t
                #if loop that checks if h is negetive
                if h < 0:
                    print("The height ended up negetive, which isn't possible unless gravity reversed.")
                    print("But if you still want the answer, it's ",h)
                else:
                    print("the height is: ", h)

            #repeats loop
            x= input("Please enter in the first value (press enter to end): ")

        #statment printed when loop is exited
        print("Program exited.")





    #if user didn't type in all three numbers
    #except NameError:
    #    print("You didn't enter in the necessary numbers! Please try again!")
    #if user didn't type in numbers as values
    #except TypeError:
    #    print("The inputs were not numbers! Please try again!")
    #if user didn't type in correct format
    #except SyntaxError:
    #    print("Your input was not in the correct format. Please try again!")
    #when an unknown error occurs
    #except:
    #   print("Oops! Something didn't work out! Please try again!")
main()
