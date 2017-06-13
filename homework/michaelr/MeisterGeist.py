import random

print("Welcome to MeisterGeist! To play input a 4 digit number. Bravo = number in correct position; Alpha = number in answer but not in correct position; Zulu = nothing correct")

master = str(random.randrange(0000, 9999))
prompts = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth", "Eleventh", "Twelth"]
inString = ""
tries = 0


def testguess(guess, key):
    s = ""
    iterator = 1
    match = False

    while iterator < len(key):

        if guess[iterator] == key[iterator]:
            s += "Bravo"
            match = True
        elif parsechar(key, guess[iterator]):
            s += "Alpha"
            match = True
        else:
            s += "-"
        iterator += 1

    if match == False:
        s = "Zulu"
    return s


def parsechar(s, char):
    i = 1
    while i < len(s):
        if s[i] == char:
            return True
        i += 1
    return False

while tries < 12:

    while len(inString) < len(master):
        inString = input(prompts[tries] + " guess: ")

    if inString == master:
        print("You win!")
        break
    else:
        print(testguess(inString, master))

    inString = ""
    tries += 1

if tries == 12:
    print("You lose!!")
