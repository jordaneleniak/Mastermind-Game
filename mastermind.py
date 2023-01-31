"""
Program: Mastermind
Author: Jordan Eleniak

This is a mastermind game. Player one enters a code and then player two has to try and
crack the code. Each attempt will yield a clue to help crack the code. Player two will be
told if they have a correct number in the correct spot or if they have a correct number
in the wrong spot.
"""
# Importing OS to clear screen to prevent Player two from seeing the code. 
import os
clear = lambda: os.system('cls') # This function will clear the screen upon a successful code entry.

## Player One starts
#
# This code block prompts Player One to enter a code and checks to make sure that it
#   is the right length.
#

## Declaring boolean test variables to make sure Player One has entered a valid code
#   and verifies that they want to use the code entered.
#

def main():
    print("Welcome to MASTERMIND!")
    print("The master code breaking game.")
    getValidCode()

    ## Player Two
    #
    # This is where Player Two tries and guess the code that Player One has picked.
    #

## Get Valid Code
#
# This function gets a valid code.
#
def getValidCode():
    try:
        masterCode = int(input("Please enter a 4 digit number: "))
        validCode = validateCode(masterCode)
        if validCode == True:
            verifyCode(masterCode)
        else:
            getValidCode() # Added a recursion loop
    except:
        print("Error: You did not enter a valid code. Please enter numbers only!")
        getValidCode() # Added a recursion loop
    return

## Validate Code
#
# This function validates the entered code.
#
def validateCode(codeToTest):
    validCode = False
    if len(str(codeToTest)) < 4:
        print("Sorry, the code you entered is too short. Please try again.")
    elif len(str(codeToTest)) > 4:
        print("Sorry, the code you entered is too long. Please try again.")
    else:
        validCode = True
    return validCode

## Verify Code
#
# This function verifies with the user that the code entered is the code
#   that they want to use.
#
def verifyCode(code):
    codeVerified = False
    print("You have entered", code, ".")
    isCodeCorrect = input("Is this the code you want? Yes/No: ").lower()
    if isCodeCorrect == 'y' or isCodeCorrect == 'yes':
        codeVerified = True
        clear()
    elif isCodeCorrect == 'n' or isCodeCorrect == 'no':
        getValidCode()
    else:
        print("Please enter yes or no.")
        verifyCode(code)
    return codeVerified

## Start the program
#
main()