#Isabella Phung
#Period 2
#Project 5.3
#File: ch5_3.py
#This program creates an acronym

def main():
    print("This is an acronym creator!")
    #asks for user input
    x= input("Please enter in a phrase to make an acronym:  ")

    #all of the execptions removed from words
    x= x.replace("the"," ")
    x= x.replace("of"," ")
    x= x.replace("and"," ")
    x= x.replace("The"," ")
    x= x.replace("Of"," ")
    x= x.replace("And"," ")
    #creates list out of user input
    x= x.split()

    #for loop that finds the first index of each value in the list created
    for i in range(len(x)):
        y= x[i]
        first= y[0]
        #prints out each letter
        print(first[0],end="")

main()
