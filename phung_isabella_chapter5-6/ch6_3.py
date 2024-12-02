#Isabella Phung
#Period 2
#Project 6.3
#File: ch 6_3.py
#This program writes out the lyrics of Bingo

def main():
    print("Hello! This program will sing you a special Bingo Song!")
    x= input("Please enter in a name of an animal!  ")
    #asks for animal value

    bingo="B-I-N-G-O"
    clap=""

    #iterates each verse of bingo
    for i in range(6):
        #first line
        print("There was a farmer, had a", x , end= "\n" "and Bingo was his name-o.")
        print("")

        #prints out the bingo part three times and connects the words with clap
        for i in range(3):
            print(clap + bingo)
        print("And Bingo was his name-o.")
        print("")
        #for loop changes clap depending on the amount of times the song has iterated
        for d in range(i-1):
            clap= clap + "(clap)-"

        #shortens the length of bingo
        bingo= bingo[2:len(bingo)]
main()



