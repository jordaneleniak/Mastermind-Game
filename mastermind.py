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
successfulCodeEntered = False
correctCode = False
while successfulCodeEntered == False:  # This code will keep looping until a valid and verified code is entered.
    try:
        playerOne = int(input("Please enter a 4 digit number: "))
        while correctCode == False:
            if len(str(playerOne)) == 4:
                print("You have entered: " + str(playerOne) + ".")
                isCodeCorrect = input("Is this the code you want? Yes/No: ").lower()
                if isCodeCorrect == 'y' or isCodeCorrect == 'yes':
                    correctCode = True
                    successfulCodeEntered = True
                    clear()
                elif isCodeCorrect == 'n' or isCodeCorrect == 'no':
                    playerOne = int(input("Please enter a new 4 digit number: "))
                else:
                    print("Please enter yes or no.")
            elif len(str(playerOne)) < 4:
                print("Code length not long enough. Please try again.")
                playerOne = int(input("Please enter a 4 digit number: "))
            elif len(str(playerOne)) > 4:
                print("Code length too long enough. Please try again.")
                playerOne = int(input("Please enter a 4 digit number: "))
    except:
        print("Error: You did not enter a valid code. Please enter numbers only!")

## Player Two
#
# This is where Player Two tries and guess the code that Player One has picked.
#