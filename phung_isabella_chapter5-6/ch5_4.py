#Isabella Phung
#Period 2
#Project 5.4
#File: ch5_4.py
#This program counts the amount of lines, words, and characters in a file

def main():
    print("Hello! This program will read a file and count the number of words and lines in the file!")
    #gathering input
    x= input("Please enter in the name of the file! Make sure it's correct and in the directory!  ")

   #counting lines
    #opens file
    Infile= open(x,"r")
    #for loop iterates each time there is a line and adds to a value to count how many lines there are
    lines=0
    for i in Infile.readlines():
        lines=lines+1
    #outputs value
    print("There are", lines, "lines in this file.")

    #counting words
    #closes and opens it to reset Infile
    Infile.close()
    Infile= open(x,"r")
    Infile= Infile.read()
    #splits Infile by word
    Infile=Infile.split()
    #for loop iterates each time there is a value in the list and adds to a value to count how many words there are
    words=0
    for i in range (len(Infile)):
        words=words+1
    #outputs value
    print("There are", words, "words in this file.")

    #with spaces
    #resets file
    Infile= open(x,"r")
    Infile= Infile.read()
    #removes new lines
    Infile.replace("\n", "")
    characters=0
    #for loop iterates each time based off of the length of the file and adds to a value to count how many character there are
    for d in range(len(Infile)):
        characters=characters+1
    print("There are", characters, "characters in this file (w/ spaces).")

    #without spaces
    #removes spaces
    Infile= Infile.replace(" ", "")
    characters=0
    #for loop iterates each time based off of the length of the file and adds to a value to count how many character there are
    for d in range (len(Infile)):
        characters=characters+1
    #outputs value
    print("There are", characters, "characters in this file (w/out spaces).")


main()
