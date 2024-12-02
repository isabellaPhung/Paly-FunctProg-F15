#Isabella Phung
#Period 2
#Project 11
#File: ch11.py
#This program does many matrix calculations


from statistics import mean

#I had attempted mode but it was so confusing and frustrating, I had to give up because I didn't have enough time
#def findMode(matrix):
    #matrixNum= 0
    #mode= "There is no mode"
    #for i in range (len(matrix)):
        #compare= matrix[matrixNum]
        #for d in matrix:
            #if compare == d:
                #mode=d
                #return mode
        #return mode

#finds determinants
def Determinant(matrix, matrixSize):
    if matrixSize == 2: #Matrix size 2
        a= matrix[0] #variable assignments for determinant equation
        b= matrix[1]
        c= matrix[2]
        d= matrix[3]
        determinant= (a*d)-(b*c) #determinant equation
        return determinant
    else:               #matrix size 3
        a= matrix[0] #variable assignments for determinant equation
        b= matrix[1]
        c= matrix[2]
        d= matrix[3]
        e= matrix[4]
        f= matrix[5]
        g= matrix[6]
        h= matrix[7]
        i= matrix[8]
        determinant= (a*e*i)+(b*f*g)+(c*d*h)-(c*e*g)-(b*d*i)-(a*f*h) #determinant equation
        return determinant

def printMatrix(matrix): #prints out Matrix properly
    rows=0
    for d in range(len(matrix)):
            print("|", matrix[rows], "|") #draws sides
            rows=rows+1

def main():
    #gathering user input
    print("This is a program that will create a user-inputed square matrix. When entering the values of the matrix, it will do it line by line.")
    matrixSize= eval(input("Please enter in the size of the square matrix: "))

    matrix= [] #this is the nested matrix
    plainMatrix= [] #this is a simple list with all of the matrix values

    #creates matrix based off of how large the matrix must be
    for i in range(matrixSize): #nests lists into list
        line= []
        for i in range(matrixSize): #makes inner lists
            x= eval(input("Please enter in one of the numbers to put into the matrix: "))
            line.append(x)
            plainMatrix.append(x)
        matrix.append(line) #nests lists
    printMatrix(matrix)

    #element changer
    change= input("Please enter in which element to change (Press Enter to continue): ")
    while change != "":
        #formats matrix numbers into index numbers
        changeFirst= eval(change[0])-1
        changeSecond= eval(change[1])-1

        newInput= eval(input("Please enter in the new value: "))
        row=matrix[changeFirst] #new row
        del row[changeSecond] #deletes old value
        row.insert(changeSecond, newInput) #inserts it in old place
        printMatrix(matrix)
        change= input("Please enter in which element to change (Press Enter to continue): ")

    #median
    plainMatrixLen= int(len(plainMatrix)/2) #length calculations
    plainMatrix = sorted(plainMatrix)   #sorts list

    #if the matrix has an even amount of values, then it will calculate the inbetween median
    if matrixSize % 2 == 0:
        plainMatrixLen= (plainMatrix[plainMatrixLen]+plainMatrix[plainMatrixLen-1])/2
        print("Median:", plainMatrixLen)
    else:   #if it has an odd amount of values, it will spit out the normal values
        print("Median: ", plainMatrix[plainMatrixLen])

    #other values
    maximum= max(plainMatrix)
    minimum= min(plainMatrix)
    average= mean(plainMatrix)
    #Mode= findMode(matrix)
    #print("Mode: ", Mode)
    print("Maximum: ", maximum)
    print("Minimum: ", minimum)
    print("Average: ", average)

    #if statement that determines if the determinant must be calculated and leads to the determinant function
    if matrixSize == 3 or matrixSize ==2:
        determinant= Determinant(plainMatrix, matrixSize)

    print("The determinant is ", determinant)





main()