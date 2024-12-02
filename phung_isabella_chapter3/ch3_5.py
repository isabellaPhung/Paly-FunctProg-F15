#Isabella Phung
#Period 2
#Project 3.5
#expected inputs are 2 separate values

def main():
    print("This program will calculate the sum of all the numbers you can enter.")
    howmany= eval(input("Please enter in the amount of numbers you want to enter:  "))
    sum=0
    for i in range(howmany):
        x= eval(input("Enter in a number to be in the sum:  "))
        sum=x+sum
    print("sum:", sum)

main()
