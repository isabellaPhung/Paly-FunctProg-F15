#Isabella Phung
#Period 2
#Project 3.6
#expected inputs are 1 single value

import math
def main():
    print("This program will estimate pi/4 depending on the amount of terms to be used.")
    x= eval(input("Please enter in the amount of terms to be used to estimate pi/4:  "))
    denom = 1
    total= 1
    odd=2
    x=x-1
    for i in range(x):
        denom=denom + odd
        denom=denom * -1
        odd=odd * -1
        total= 1/denom + total


    error= (math.pi/4) - total
    print("The difference error is: ", error)
    print("The approximation is: ", total)
main()