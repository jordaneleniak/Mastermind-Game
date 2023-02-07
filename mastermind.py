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

    totalNumberOfGuessesAllowed = 20
    codeLength = 4
    welcome()
    while endOfGame == False:
        numberOfGuesses = 0
        masterCode = int(getValidCode(codeLength))
        clear()
        print("Player two, try and guess the code player one has chosen.")
        while successfulCrack == False and numberOfGuesses <= totalNumberOfGuessesAllowed:
            testCode = int(getValidCode(codeLength))
            resultOfTest = compareCodes(masterCode, testCode)
            successfulCrack = resultOfTest[0]
            codeHint = resultOfTest[1]
            print(codeHint)
            print(masterCode, testCode) # TODO Delete this line of code, only here for testing purposes!
            numberOfGuesses += 1
            print(numberOfGuesses)
        if testCode == masterCode:
            if numberOfGuesses <= totalNumberOfGuessesAllowed:
                playerTwoScore += 1
        else:
            playerOneScore += 1
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
def getValidCode(codeLength):
    try:
        code = int(input("Please enter a 4 digit number: "))
        validCode = validateCode(codeLength, code)
        if validCode == True:
            verifyCode(codeLength, code)
        else:
            getValidCode(codeLength) # Added a recursion loop
    except:
        print("Error: You did not enter a valid code. Please enter numbers only!")
        getValidCode(codeLength) # Added a recursion loop
    return code

## Validate Code
#
# This function validates the entered code.
#
def validateCode(codeLength, codeToTest):
    validCode = False
    if len(str(codeToTest)) < codeLength:
        print("Sorry, the code you entered is too short. Please try again.")
    elif len(str(codeToTest)) > codeLength:
        print("Sorry, the code you entered is too long. Please try again.")
    else:
        validCode = True
    return validCode

## Verify Code
#
# This function verifies with the user that the code entered is the code
#   that they want to use.
#
def verifyCode(codeLength, code):
    codeVerified = False
    print("You have entered", code, ".")
    isCodeCorrect = input("Is this the code you want? Yes/No: ").lower()
    if isCodeCorrect == 'y' or isCodeCorrect == 'yes':
        codeVerified = True
    elif isCodeCorrect == 'n' or isCodeCorrect == 'no':
        getValidCode(codeLength)
    else:
        print("Please enter yes or no.")
        verifyCode(codeLength, code)
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
        hint = testCode
    else:
        hint = getCodeHint(masterCode, testCode)
    return successfulCrack, hint

## Get Code Hint
#
# This function returns a hint to the player to help them crack the master code. If the player
#   has a correct number in the right spot, it returns an 'x'. If the player has a correct
#   number in the wrong spot, it returns an 'o'.
#
def getCodeHint(masterCode, testCode):
    hint = []
    masterCode = str(masterCode)
    testCode = str(testCode)
    for i in range(4):
        if masterCode[i] == testCode[i]:
            hint.append("x")
        else:
            for j in range(4):
                if masterCode[i] == testCode[j]:
                    hint.append("o")
    hint = str(hint)
    return hint

## Start the program
#
main()