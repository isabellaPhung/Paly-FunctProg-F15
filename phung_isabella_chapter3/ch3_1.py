#Isabella Phung
#Period 2
#Project 3.1
#expected inputs are 2 separate values

import math
def main():
    print("Hello! I am a cylinder volume and surface area calculator!")
    r= eval(input("Please enter in the radius of the cylinder:  "))
    h= eval(input("Please enter in the height of the cylinder:  "))
    v=  (math.pi)*(r*r)*h
    sa= 2*math.pi*r*(h+r)
    print("The volume is: ", v)
    print("The surface area is: ", sa)
main()
