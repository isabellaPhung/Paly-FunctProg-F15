#Isabella Phung
#Period 2
#Project 8.3
#File: ch8_3.py
#This program shows the user how the Fermat theory is correct

def main():
    try:

        integer= input("Please enter in the integer (press enter to quit): ")

        while integer != "":
            prime= input("Please enter in the prime number : ")
            integer=eval(integer)
            prime=eval(prime)
            if integer!=int(integer):
                print("You didn't enter in an integer! Please try again!")
            else:
                if prime/2==int(prime/2):
                    print("You didn't type in a prime number! Please try again!")
                else:
                    print("step one:")
                    print(integer, "**", prime ,"-", integer)

                    print("step two:")
                    print(integer**prime, "-", integer)

                    print("step three:")
                    print(integer**prime-integer)

                    print(integer**prime-integer, "is a factor of", prime)

                    print("step four:")
                    print((integer**prime-integer),"/",prime)

                    print("step five:")
                    print((integer**prime-integer) / prime)
                    print("As you can see,", (integer**prime-integer), "is evenly divisible by", prime, "so", prime, "is a factor of", (integer**prime-integer))
                    print("Therefore Fermat's theorum is correct")

            integer= input("Please enter in the integer (press enter to quit): ")

        print("Program ended.")

    #if user didn't type in all three numbers
    except NameError:
        print("You didn't enter in the necessary numbers! Please try again!")
    #if user didn't type in numbers as values
    except TypeError:
        print("The inputs were not numbers! Please try again!")
    #if user didn't type in correct format
    except SyntaxError:
        print("Your input was not in the correct format. Please try again!")
    #when an unknown error occurs
    except:
        print("Oops! Something didn't work out! Please try again!")
main()