# A Guess The Number Game

import random

print("I'm thinking of a number between 1 - 20. Guess it!")

secretNumber = random.randint(1,20);

inputStr = input()
inputNum = int(inputStr)
numOfGuesses = 0

while(True):
    if(secretNumber == inputNum):
        print("You got the number right! Congrats!")
        print("It took you " + str(numOfGuesses) + " guesses!")
        break
    elif(secretNumber > inputNum):
        print("The number is bigger than your input! Try again!")
    elif(secretNumber < inputNum):
        print("The number is smaller than your input! Try again!")
    inputStr = input()
    inputNum = int(inputStr)
    numOfGuesses = numOfGuesses + 1
