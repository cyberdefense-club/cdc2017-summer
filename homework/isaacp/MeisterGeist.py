import random

# Set values for random choosing
randList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Sets defaults for random variables used in the program
length = 4
maxGuesses = 12
playerGuessCorrect = False
isOneCorrect = False
numbersBravo = []
numbersAlpha = []
output = ""
counter = 1


# Checks the ALPHA list against the BRAVO list to remove duplicates from the ALPHA list
def checkBravo():
    hasPopped = True
    while hasPopped:
        hasPopped = False
        for var1 in range(len(numbersBravo)):
            for var2 in range(len(numbersAlpha)):
                if numbersBravo[var1] == numbersAlpha[var2]:
                    hasPopped = True
                    numbersAlpha.pop(var2)
                    break


# Clears any repeating numbers from the ALPHA list by comparing it against itself, then the return list
def clearOverlapingNumbers(list1, list2):
    checkAll = False
    firstRun = True
    comparison = [0]
    for x in range(len(list1)):
        for y in range(len(list2)):
            if list1[x] == list2[y]:
                for z in range(len(comparison)):
                    if list1[x] != comparison[z]:
                        if firstRun:
                            comparison.clear()
                            firstRun = False
                    else:
                        checkAll = True
                if not checkAll:
                    comparison.append(list1[x])
                else:
                    checkAll = False
    numbersAlpha.clear()
    return comparison

# Sees if the user wants to change how many guesses he gets
while True:
    start = input("How many guesses do you want? (type default to use the default settings): ")
    if start.lower() != "default":
        try:
            maxGuesses = int(start)
            break
        except ValueError:
            print("Please type in an integer number or default")
    else:
        break
    del start

# Sees if the user wants to change how many numbers he has to guess
while True:
    start = input("How long of a guess do you want? (type default to use the default settings): ")
    if start.lower() != "default":
        try:
            length = int(start)
            break
        except ValueError:
            print("Please type in an integer number or default")
    else:
        break
    del start
# Sets the number to guess
randomNum = ""
for randRange in range(length):
    randomNum = randomNum + random.choice(randList)

# The main program
while not playerGuessCorrect and counter != maxGuesses + 1:
    print("\nGuess #{0}".format(counter))
    # Get player guess
    playerGuess = str(int(input("Give me a {0} digit number: ".format(length))))

    # Check for correct positioning and correct number
    for x in range(len(randomNum)):
        for y in range(len(playerGuess)):
            if randomNum[x] == playerGuess[y]:
                isOneCorrect = True
                if x == y:
                    numbersBravo.append(y)
                    numbersAlpha.append(y)
                else:
                    numbersAlpha.append(y)

    # Checks if you got a correct answer
    if isOneCorrect:
        checkBravo()

        # Prevents an ALPHA showing up when the ALPHA list is empty
        try:
            if numbersAlpha[0] != None:
                numbersAlpha = clearOverlapingNumbers(numbersAlpha, numbersAlpha)
        except IndexError:
            somethingToDoToNotThrowAnError = "NeverUsed"

        # Formats the output string with ALPHAs and BRAVOs
        for z in range(len(numbersAlpha)):
            output = output + "ALPHA "
        for a in range(len(numbersBravo)):
            output = output + "BRAVO "
    else:
        output = "ZULU"
    print("\n" + output)

    # Checks if you guessed the number correctly
    if playerGuess == randomNum:
        playerGuessCorrect = True
        print("\nYou guessed my number!")

    # Clears the lists and the output and increments the counter
    numbersBravo.clear()
    numbersAlpha.clear()
    del output
    output = ""
    counter += 1
if counter == maxGuesses:
    print("\nToo bad, you lost. Better luck next time!")