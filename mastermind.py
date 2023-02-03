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

## Player Two
#
# This is where Player Two tries and guess the code that Player One has picked.
#

## Declaring boolean test variables to make sure Player One has entered a valid code
#   and verifies that they want to use the code entered.
#

## Main Function
#
# The main function controls the game and tracks scores.
#
def main():
    # Forcing player scores to be ints
    playerOneScore = int(0)
    playerTwoScore = int(0)
    # Declaring test booleans to check for end of game and a successfully cracked master code.
    endOfGame = False
    successfulCrack = False
    welcome()
    while endOfGame == False:
        masterCode = int(getValidCode())
        print("Player two, try and guess the code player one has chosen.")
        while successfulCrack == False:
            testCode = int(getValidCode())
            resultOfTest = compareCodes(masterCode, testCode)
            successfulCrack = resultOfTest[0]
            codeHint = resultOfTest[1]
            print(codeHint)
            print(masterCode, testCode)
        endOfGame = keepPlaying()
    print("Final scores!")
    displayScores(playerOneScore, playerTwoScore)
    print("Thank you for playing!")

## Welcome splash screen
#
# This function is for the welcome splash screen. This is a separate function to make changing the welcome message easier.
#
def welcome():
    print("Welcome to MASTERMIND!")
    print("The master code breaking game.")

def displayScores(playerOneScore, playerTwoScore):
    print("Player One:", playerOneScore)
    print("Player Two:", playerTwoScore)

## Get Valid Code
#
# This function gets a valid code.
#
def getValidCode():
    try:
        code = int(input("Please enter a 4 digit number: "))
        validCode = validateCode(code)
        if validCode == True:
            verifyCode(code)
        else:
            getValidCode() # Added a recursion loop
    except:
        print("Error: You did not enter a valid code. Please enter numbers only!")
        getValidCode() # Added a recursion loop
    return code

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

## Keep Playing
#
# This function tests to see if the players want to keep playing or not
#
def keepPlaying():
    endOfGame = False
    keepPlaying = input("Do you wish to keep playing? Yes/No ").lower()
    while keepPlaying not in['yes', 'y', 'no', 'n']:
        print("Please enter yes or no.")
        keepPlaying = input("Do you wish to keep playing? Yes/No ").lower()
    if keepPlaying == 'no' or keepPlaying == 'n':
        endOfGame = True
    return endOfGame

## Compare codes
#
# This function will compare the code player 2 entered against the master code player one chose.
#

def compareCodes(masterCode, testCode):
    successfulCrack = False
    if masterCode == testCode:
        successfulCrack = True
    else:
        hint = getCodeHint(masterCode, testCode)
    return successfulCrack, hint

def getCodeHint(masterCode, testCode):
    hint = "temp"
    for i in masterCode:
        if masterCode[i] == testCode[i]:
            hint[i] = testCode[i]
        else:
            for j in testCode:
                pass   
    return hint


## Start the program
#
main()