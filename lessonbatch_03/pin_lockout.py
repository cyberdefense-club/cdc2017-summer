import getpass
import time


def flash_string(flashstring="...", flashreps=5, flashsleep=0.5):
    BACKSPACE = "\b"
    SPACE = " "

    """make it look like we are doing work by flashing text"""

    fslength = len(flashstring)

    for i in range(flashreps):
        print("{0}{1}".format(
            # don't bother on the first loop:
            SPACE * (fslength if i else 0),
            BACKSPACE * (fslength if i else 0)),
            end="", flush=True)

        time.sleep(flashsleep)

        print("{0}{1}".format(
            flashstring,
            BACKSPACE * fslength),
            end="", flush=True)
        time.sleep(flashsleep)

    # print("{0}{1}{0}".format(
    #     SPACE * fslength,
    #     BACKSPACE * fslength),
    #     end="", flush=True)


def get_masked_int_password(prompt, errormsg, min_int, max_int, min_len=None, max_len=None,
                            sleep_every=None, sleep_length=None, sleep_penalty=None, PIN=None):

    tries = 0
    sleeping_msg = "   ...sleeping..."

    while True:
        tries += 1
        instring = getpass.getpass(prompt)

        if instring == str(PIN):
            print("done!")
            return True
        else:
            print(errormsg)
            if tries == 3:
                print(f"Failure number {tries}. The screen will now lock for {sleep_length} seconds.\n")
                flash_string(sleeping_msg, sleep_length, 0.5)
                tries = 0
                try:
                    new_sleep_length = int(eval(str(sleep_length) + str(sleep_penalty)))
                    sleep_length = max(sleep_length, new_sleep_length)
                except SyntaxError:
                    print("oops")
                    pass
                except ZeroDivisionError:
                    print("oops2")
                    pass
            else:
                print(f"Failure number {tries}. The screen will lock at {sleep_every} failures.\n")


def main():
    pin = "12345"

    while True:
        print("")
        pwd = get_masked_int_password(
            prompt='Please enter a 5-digit number: ',
            errormsg="You have not entered the correct PIN. Please try again.",
            min_int=0,
            max_int=99999,
            min_len=5,
            max_len=5,
            sleep_every=3,
            sleep_length=2,
            sleep_penalty="*2",
            PIN=pin
        )
        print("You have entered the correct PIN. Thank you.")


if __name__ == '__main__':
    main()
