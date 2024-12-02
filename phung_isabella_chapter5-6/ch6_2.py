#Isabella Phung
#Period 2
#Project 6.2
#File: ch6_2.py
#This program creates a grid

def horizontal():
    #for loop that iterates twice and creates horizontal line
    for d in range(2):
        x= print("+" , "-", "-", "-", "-", end= " ")
    #caps off the line
    print("+", "")

def vertical():
    #for loop that iterates 4 times to create vertical lines
    for i in range(4):
        print("|         |         |")

#main method that iterates everything
def main():
    horizontal()
    vertical()
    horizontal()
    vertical()
    horizontal()
main()


