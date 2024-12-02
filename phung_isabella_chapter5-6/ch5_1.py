#Isabella Phung
#Period 2
#Project 5.1
#File: ch5_1.py
#This program calculates quiz scores

def main():
    #asks for user input
    s=eval(input("Please enter in a math exam score!"))
    #creates a list based off of the grades available, because there are exactly 13 grades possible
    grades= ['F','F+','D-','D','D+','C-','C','C+','B-','B','B+','A-','A','A+']
    #prints out the index value of the above list
    print(grades[s])
main()
