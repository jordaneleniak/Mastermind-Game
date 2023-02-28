"""
Program: Mastermind
Author: Jordan Eleniak

This is a digital copy of the board game Mastermind.

Player One chooses the master code. The mastercode has to be 4 ints long. The game
    will then verify the validated code. Once validated, the player will be prompted if
    that's the code they want to use. If not, the player will have to keep entering a new
    code until they enter one they want to use.

Player Two tries and guess the code that Player One has picked. The code undergoes the same
    validation and verification as player one. Once player two enters a valid code that they
    want to try, the game will then compare the two codes.

The code checking process compares each number in the mastercode against each number in the
    test code. If player two has a correct number in the correct spot, the game assigns 'x'
    to a variable called hint. If player two has a correct number in the wrong spot, the
    game assigns 'o' to the variable hint.

The game then displays the hint to help the player narrow down possibilities. Player two has
    20 attempts to try and crack the mastercode player one has chosen. If they crack the master
    code in 20 attempts or less, player two gets a point. Otherwise player one gets a point.
"""
# Importing OS to clear screen to prevent Player two from seeing the code. 
import os
clear = lambda: os.system('cls') # This function will clear the screen upon a successful code entry.

## Main Function
#
# The main function controls the game and tracks scores.
#
def main():
    # Forcing player scores to be ints
    playerOneScore = int(0)
    playerTwoScore = int(0)
    gameRound = int(0)
    # Declaring test booleans to check for end of game and a successfully cracked master code.
    endOfGame = False
    successfulCrack = False

    codeLength = 4
    welcome()
    while endOfGame == False:
        gameRound += 1
        totalNumberOfGuessesAllowed = 20
        masterCode = getValidCode(codeLength)
        clear()
        print("Player two, try and guess the code player one has chosen.")
        while successfulCrack == False and  totalNumberOfGuessesAllowed != 0:
            codeHint = ''
            testCode = getValidCode(codeLength)
            resultOfTest = compareCodes(masterCode, testCode)
            successfulCrack = resultOfTest[0]
            codeHint = resultOfTest[1]
            print(codeHint)
            print(masterCode, testCode) # TODO Delete this line of code, only here for testing purposes!
            totalNumberOfGuessesAllowed -= 1
            if totalNumberOfGuessesAllowed != 0:
                print("Number of guesses remaining: " + str(totalNumberOfGuessesAllowed))
            else:
                print("Sorry, the number was " + str(masterCode))
        if (gameRound % 2) == 0:
            if testCode == masterCode:
                if totalNumberOfGuessesAllowed == 0:
                    playerOneScore += 1
            else:
                playerTwoScore += 1
        else:
            if testCode == masterCode:
                if totalNumberOfGuessesAllowed == 0:
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

## Display Scores
#
# This function displays the scores.
#
def displayScores(playerOneScore, playerTwoScore):
    print("Player One:", playerOneScore)
    print("Player Two:", playerTwoScore)

## Get Valid Code
#
# This function gets a valid code.
#
def getValidCode(codeLength):
    code = int(0000)
    # swap recursion in this function to a while loop to fix the out of bounds error.
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
    if isCodeCorrect[0] == 'y':
        codeVerified = True
    elif isCodeCorrect[0] == 'n':
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
    while keepPlaying[0] not in['y', 'n']:
        print("Please enter yes or no.")
        keepPlaying = input("Do you wish to keep playing? Yes/No ").lower()
    if keepPlaying[0] == 'n':
        endOfGame = True
    return endOfGame

## Compare codes
#
# This function will compare the code player 2 entered against the master code player one chose.
#
def compareCodes(masterCode, testCode):
    successfulCrack = False
    if masterCode != testCode:
        hint = getCodeHint(masterCode, testCode)
    else:
        successfulCrack = True
        hint = testCode
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
        if masterCode[i] != testCode[i]:
            for j in range(4):
                if testCode[j] == masterCode[i]: hint.append("o")
        else:
            hint.append("x")
    hint = str(hint)
    return hint

## Start the program
#
main()