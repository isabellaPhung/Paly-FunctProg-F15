#Isabella Phung
#Period 2
#Project 3.2
#expected inputs are 3 separate values

def main():
    print("Rocko's Ice Cream is the best dessert food truck around! They cater based off of distance and taco topping! This will help calculate the cost!")
    distance = eval(input("Please enter the distance between the catering destination and the Rocko's Ice Cream Truck:  "))
    howmany= eval(input("Please enter in how many tacos you want:  "))
    topping = eval(input("Please enter in the amount of different toppings:  "))
    total= (3.75*howmany)+(topping*0.5)+20+(0.5*distance)
    print("Here is the total:  ", total)
main()