#Isabella Phung
#Period 2
#Project 5.5
#File: ch5_5.py
#This program creates an amortization table

def main():
    print("Hello! This is an amoritization calculator! It will calculate the montly payment, intrest total, and principal for each month!")

#asking for values
    principal= eval(input("Please enter in the initial amount: "))
    downPayment= eval(input("Please enter in the down payment: "))
#calculating the actual principal
    principal=principal-downPayment
    intrestRate= eval(input("Please enter in the annual interest rate: "))
    numYears= eval(input("Total number of years: "))

#calculates the amount of payments in total
    payments= numYears*12
#converts annual intrest rate to months
    monthInt= (intrestRate/100)/12
#calculates the amount of total pay per month
    MonthPay= (monthInt*principal*(1+monthInt)**payments)/((1+monthInt)**payments-1)

#calculates the amount of money going to the interest each monthly payment
    toInterest=principal*monthInt
#calculates the amount of money going to the mortgage each monthly payment
    toMorgage=MonthPay-toInterest

#Loop that makes table
    for i in range(payments+1):
#rounding all of the values
        MonthPay= round(MonthPay, 2)
        toMorgage= round(toMorgage, 2)
        toInterest= round(toInterest, 2)

#printing of values
        print(i+1, end= "\t\t")
        print(MonthPay, end= "\t\t")
        print(toMorgage, end= "\t\t")
        print(toInterest, end= "\t\t")

#changes principal amount
        principal= principal-toMorgage
#rounds principal amount
        principal=round(principal,2)
#changes toInterest to be based off of the principal amount
        toInterest=principal*monthInt
#changes toMorgage to be based off of the principal amount
        toMorgage=MonthPay-toInterest

        #print(",[0,0.2f},").format(principal)
        #I had attempted to use round, but I needed it to round down.
        #When I used it, it skewed the numbers too much.
        #But it was the only way I could get two decimals
        #I also attempted to use the format method, but it did not work for some reason.

#ensures that principal will not be a negetive number
        if principal>0:
            print(principal)
        else:
            print(0)


main()