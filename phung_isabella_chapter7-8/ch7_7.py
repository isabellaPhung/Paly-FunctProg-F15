#Isabella Phung
#Period 2
#Project 7.7
#File: ch7_7.py
#This program calculates percent error of a rectangular prism

#function to calculate the maximum values
def maximum(height, width, depth):
    #places 5 at the end so it is properly rounded
    height= height + "5"
    #then converts to a float
    maximumHei= eval(height)
    width= width + "5"
    maximumWid= eval(width)
    depth= depth + "5"
    maximumDep= eval(depth)
    return maximumHei, maximumWid,maximumDep

#function to calculate the minimum values
def minimum(height, width, depth):
    #places 5 at the end so it is properly rounded
    height= height + "5"
    #converts to float
    height= eval(height)
    #subtracts one from the 10s place so it is properly rounded
    minimumHei=height-0.1
    width= width + "5"
    width= eval(width)
    minimumWid=width-0.1
    depth= depth + "5"
    depth= eval(depth)
    minimumDep=depth-0.1
    return minimumHei, minimumWid,minimumDep

def main():
    try:
        #gathers user input
        height = input("Please enter in the height: ")
        width = input("Please enter in the width: ")
        depth = input("Please enter in the depth: ")

        #if all of the numbers are decimals it will perform the first section of this if statement
        #it did not specify in the problem if all or only some of the numbers had to be floats, so I assumed all had to be floats
        if eval(height) != int(eval(height)) and eval(width) != int(eval(width)) and eval(depth) != int(eval(depth)):
            #initiates functions to calculate minimum and maximum values
            maximumHei, maximumWid, maximumDep= maximum(height, width, depth)
            minimumHei, minimumWid,minimumDep= minimum(height, width, depth)

            #evaluates values
            height= eval(height)
            width= eval(width)
            depth= eval(depth)
            #plugs into measured value equation
            measured= height*width*depth
            #minimum value equation
            minimum1= minimumHei* minimumWid*minimumDep
            #maximum value equation
            maximum1= maximumHei*maximumWid*maximumDep
            #minimum percent error equation
            minimumPer=abs(minimum1-measured)/measured
            #maximum percent error equation
            maximumPer=abs(maximum1-measured)/measured

        #if most of the numbers are not decimals, then it initiates this latter part of the if statement
        else:
            #evaluates values
            height=eval(height)
            width=eval(width)
            depth=eval(depth)
            #plugs into measured value equation
            measured= height*width*depth
            #minimum value equation
            minimum2= (height-0.5)*(width-0.5)*(depth-0.5)
            #maximum value equation
            maximum2= (height+0.5)*(width+0.5)*(depth+0.5)
            #minimum percent error equation
            minimumPer=abs(minimum2-measured)/measured
            #maximum percent error equation
            maximumPer=abs(maximum2-measured)/measured



        #checks for greatest percent error and prints it
        if minimumPer > maximumPer:
            print("the greatest possible percent error is", minimumPer)
        else:
            print("The greatest possible percent error is", maximumPer)





        #if user didn't type in all necessary numbers
    except NameError:
        print("You didn't enter in the necessary numbers! Please try again!")
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