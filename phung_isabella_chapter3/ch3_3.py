#Isabella Phung
#Period 2
#Project 3.3
#expected inputs are 2 separate values

import math
def main():
    print("This program will calculate the distance between 2 points in a 3 dimensional plane.")
    x1,y1,z1 = eval(input("Please enter in the first point, with each axis separated by a comma:  "))
    x2,y2,z2 = eval(input("Please enter in the second point, with each axis separated by a comma:  "))
    distance= math.sqrt((x2-x1)**2 + (y2-y1)**2+(z2-z1)**2)
    print("The distance is: ", distance)

main()