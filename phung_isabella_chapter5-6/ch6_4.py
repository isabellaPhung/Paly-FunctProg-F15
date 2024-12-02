#Isabella Phung
#Period 2
#Project 6.4
#File: ch6_4.py
#This program calculates the percentage error of an estimated infinate series vs. an actual infinate series

#calcuates result
def actualresult(term3, ratio3):
    result = term3/(1-ratio3)
    return result

#calculates estimate
def estimate(term2, ratio2, num):
    total= 9
    #adds term 2 to total depending on how many terms desired
    for i in range(num-1):
        term2=term2*ratio2
        total=total+term2
    return total

#main method
def main():
    print("Hello! This program will calculate the estimated result, real result, and error difference of an infinite series!")
    #gathers user input
    term1 = eval(input("Please enter in the first term: "))
    ratio1 = eval(input("Please enter in the common ratio: "))
    terms = eval(input("Please enter in the number of terms: "))

    #inputs user input values into outside methods
    estimateresult = estimate(term1, ratio1, terms)
    realResult = actualresult(term1, ratio1)
    #calculates error
    error = abs(estimateresult - realResult)

    #prints outputs
    print("The estimated result is", estimateresult)
    print("The real result is", realResult)
    print("The amount of error is", error)
    
main()
