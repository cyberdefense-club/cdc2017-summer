from random import randint;

# generate list of 4 random numerals
def generate_secret():
    
    secret = []
    
    for i in range(4):
        secret.append(str(randint(0, 9)))
    
    return secret

#compare input to secret and return hint string
def generate_hint(secret, guess):
    hint = ''

    #create a copy of secret to modify, cuz apparently it accesses the string from main
    secretCopy = secret[:]

    # Process bravo first
    for digit in range(len(guess)):

        if secretCopy[digit] == guess[digit]:
            hint = hint + "BRAVO "
            secretCopy[digit] = ' '

    # Process alpha second
    for digit in range(len(guess)):

        if guess[digit] in secretCopy:
            hint = "ALPHA " + hint
            secretCopy[secretCopy.index(guess[digit])] = ' '
    
    # If there were no alphas or bravos, zulu
    if hint == '':
        hint = "ZULU"

    return hint

def main():
    # generate number
    secret = generate_secret();

    print(secret)

    # ask for number of guesses
    max_guesses = int(input("How many guesses should you get? (#1 doctor reccomended value is 12!): "))
    num_guesses = 0

    correct = False

    # loop while guess != secret and number of guesses <= max
    while not correct and num_guesses < max_guesses:
        guess = list(input("What is your guess?: "))

        # test input and output hints
        if guess == secret:
            correct = True
        else:
            print(generate_hint(secret, guess))

        num_guesses += 1

    # Congratulate/fail
    if correct:
        print("You win... yay.")
    else:
        print("You lose... yay.")

main()
