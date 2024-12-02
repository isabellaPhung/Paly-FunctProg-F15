#Isabella Phung
#Period 2
#Project 6.5
#File: ch6_5.py
#This program calculates the percent error of estimated areas vs. the actual areas

#takes in length and width as values
def calcArea(length, width):
    #simple area calculator
    Area= length * width
    return Area

#takes in estimated area and actual area as values
#calculates percent error
def percentError(estArea, Area):
    error= (abs(estArea-Area)/estArea) * 100
    error= round(error,2)
    return error
#when tested with the given example in the assignment sheet, it was off by about 0.2 percent,
#however when I checked the work on a calculator, it was the same as my program.

def main():
    print("Hello! This program will calculate the percent error of estimated areas vs. the actual areas!")

    #asks for estimated values
    estLength= eval(input("Please input the estimated length: "))
    estWidth= eval(input("Please input the estimated width: "))

    #puts variables into calcArea method
    estArea= calcArea(estLength,estWidth)

    #asks for actual values
    length= eval(input("Please input the actual length: "))
    width= eval(input("Please input the actual width: "))

    #places variables into calcArea
    Area= calcArea(length, width)

    #enters area values from calcArea into error calculator
    error= percentError(estArea, Area)

    #outputs values
    print("The estimated area is ", estArea, "units squared")
    print("The actual area is ", Area, "units squared")
    print("The precent error is ", error, "%")

main()
