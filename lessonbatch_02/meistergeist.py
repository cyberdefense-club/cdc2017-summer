import time
import random

"""One implementation of MeisterGeist. Summer 2017 Python class, CRAHS CDC. See
https://github.com/cyberdefense-club/cdc2017-summer/blob/master/02-homework.txt"""

# define quasi-constants:
ALPHA = "ALPHA"
BRAVO = "BRAVO"
ZULU = "ZULU"
SPACE = " "
BACKSPACE = "\b"
MINDIGITS = 1
MAXDIGITS = 8
MINGUESSES = 5
MAXGUESSES = 20
CORRECT = "CORRECT"
FEEDBACK = "FEEDBACK"
CONGRATS = "Congratulations! You win!!!\n"
SORRY = "Too bad, you lost. Better luck next time!\n"
WIN = 0
LOSS = 1


def generate_secret(length):
    global secret

    secret = ""

    for i in range(length):
        secret += str(random.randint(0, 9))

    return secret


def ordinal(n):
    """calculate ordinal string for n: 1st for 1, 2nd for 2, etc"""

    suffix = ['th', 'st', 'nd', 'rd', 'th', 'th', 'th', 'th', 'th', 'th']

    # ensure n is an integer >= 0:
    if n < 0:
        n *= -1
    n = int(n)

    # main magic:
    s = 'th' if n % 100 in (11, 12, 13) else suffix[n % 10]

    return str(n) + s


def evaluate_guess(guess, bravo_target):
    alpha_target = bravo_target
    n_alpha = n_bravo = 0

    # save for later:
    lengthcheck = True if len(guess) == len(bravo_target) else False

    # calculate bravo matches first, because they have higher priority:
    for c1, c2 in zip(guess, bravo_target):
        if c1 == c2:
            n_bravo += 1
            # this prevents us from alpha-matching c1 in alpha_target
            # in the future (prevents double-counting):
            alpha_target = alpha_target.replace(c1, '', 1)

            # this prevents us from alpha matching c1 from guess in the
            # future. note that this will not change the value of zip()
            # that we are iterating over.
            guess = guess.replace(c1, '', 1)

    # calculate alpha matches for letters that are not bravo-matched in either
    # guess or alpha_target:
    for c1 in guess:
        if c1 in alpha_target:
            n_alpha += 1
            # one final place to prevent double-counting:
            alpha_target = alpha_target.replace(c1, '', 1)

    evaluation = "{0}{1}{2}" \
        .format(((ALPHA + ' ') * n_alpha).strip(),
                ' ' if n_alpha > 0 else '',
                ((BRAVO + ' ') * n_bravo).strip())
    if n_alpha + n_bravo == 0:
        evaluation = ZULU

    return {
        FEEDBACK: evaluation,
        CORRECT:
            True if (n_bravo == len(bravo_target)) and lengthcheck
            else False
    }


def get_int_input(prompt, min_int, max_int,
                  min_len=None,
                  max_len=None):
    if min_len is None:
        min_len = len(str(min_int))

    if max_len is None:
        max_len = len(str(max_int))

    if min_len == max_len:
        length_msg = "{0} digits".format(max_len)
    else:
        length_msg = "{0} to {1} digits".format(min_len, max_len)
    while True:
        instring = input(prompt)

        if instring.isdigit():
            intval = int(instring)
            if intval < min_int or intval > max_int:
                print('Error - please provide an integer between {0} and {1}.'
                      .format(min_int, max_int))
            elif len(str(instring)) < min_len \
                    or len(str(instring)) > max_len:
                print('Error - please enter a number with {0}'
                      .format(length_msg))
            else:
                return instring
        else:
            print('{} is not an integer. Please try again.\n'
                  .format(instring))


def flash_dots(flashstring="...", flashreps=5, flashsleep=0.5):
    """make it look like we are doing work by flashing text"""

    fslength = len(flashstring)

    for i in range(flashreps):
        print("{0}{1}".format(
            # don't bother with the backspaces on the first loop:
            BACKSPACE * (fslength * 1 if i else 0),
            SPACE * fslength), end="", flush=True)
        time.sleep(flashsleep)

        print("{0}{1}".format(
            BACKSPACE * fslength,
            flashstring), end="", flush=True)
        time.sleep(flashsleep)

    print("{0}{1}{0}".format(
        BACKSPACE * fslength,
        SPACE * fslength), end="", flush=True)


def main(secret_length=None, secret=None, max_guesses=None, guesses=None):
    print("\nWelcome to MeisterGeist!")

    if secret_length is None:
        secret_length = int(get_int_input(
            "How many digits should the secret be? ({0}-{1}) "
                .format(MINDIGITS, MAXDIGITS), MINDIGITS, MAXDIGITS))

    print("Please wait while I generate a secret {0}-digit number..."
          .format(secret_length))

    if secret is None:
        secret = generate_secret(secret_length)

    # just flash the string "..." to make it look like we're cogitating:
    if guesses is None:
        flash_dots(flashstring="...", flashreps=5, flashsleep=0.5)
    print("Ready!\n")

    if max_guesses is None:
        max_guesses = int(get_int_input(
            "How many guesses would you like? ({0}-{1}) "
                .format(MINGUESSES, MAXGUESSES), MINGUESSES, MAXGUESSES))
        print()

    for i in range(max_guesses):
        # TODO: (1/2) make get_int_input() honor min/max values
        # TODO: (2/2) as well as min/max lengths:
        if guesses is None:
            guess = get_int_input(
                "What is your {0} guess? "
                    .format(ordinal(i + 1)), 0, 10 ** secret_length - 1,
                secret_length, secret_length)
            evaluation = evaluate_guess(guess, secret)
        else:
            evaluation = evaluate_guess(guesses[i], secret)
        print(evaluation[FEEDBACK] + "\n")

        if evaluation[CORRECT]:
            print(CONGRATS)
            return WIN

    print("The correct answer was: {0}".format(secret))
    print(SORRY)
    return LOSS


secret_length = None
secret = None
max_guesses = None
guesses = None

if __name__ == '__main__':
    main()
