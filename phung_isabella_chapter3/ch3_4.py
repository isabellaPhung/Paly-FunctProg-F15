#Isabella Phung
#Period 2
#Project 3.4
#expected inputs are 1 single value

def main():
    print("The Gregorian epact is the number of days between Jan 1st and the last new moon. This program will calculate the value of the epact.")
    year= eval(input("Please enter in the year for the epact:  "))
    C= year//100
    epact= (8 + (C//4) - C + ((8*C+13)//25)+11*(year%19))%30
    print("The epact is:  ", epact)
main()
