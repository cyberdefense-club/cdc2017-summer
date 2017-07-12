import random

print("Welcome to MeisterGeist! To play input a 4 digit number. Bravo = number in correct position; Alpha = number in answer but not in correct position; Zulu = nothing correct")

master = str(random.randrange(0000, 9999))
prompts = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth", "Eleventh", "Twelth"]
inString = ""
tries = 0


def testguess(guess, key):
    s = ""
    bCount = 0
    aCount = 0
    aKey = ''
    aGuess = ''
    match = False

    for n in range(0, len(key)):
        if guess[n] == key[n]:
            bCount += 1
            match = True
        else:
            aKey += key[n]
            aGuess += guess[n]

    for m in range(0, len(aKey)):
        if parsechar(aKey, aGuess[m]):
            aCount += 1
            aKey.pop(m)
            m -= 1
            match = True

    if match == False:
        s = "Zulu"
    else:
        j = 0
        while j < bCount:
            s += "Bravo"
        k = 0
        while k < aCount:
            s += "Alpha"

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
