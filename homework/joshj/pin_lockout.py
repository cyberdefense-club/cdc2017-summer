from getpass import getpass
from time import sleep
import multiprocessing
import sys

ATTEMPTS_BETWEEN_LOCKOUT = 3
USER_STILL_WANTS_TO_TALK = True
EXIT = "00000"
TIMEOUT = 15


def chatbot():
    sys.stdout = open(1, 'w')
    sys.stdin = open(0, 'r')

    print("\nWelcome to Illustriously Secure Chat Bot (tm).")

    # User never wants to stop talking, so USER_STILL_WANTS_TO_TALK is a constant. 
    while USER_STILL_WANTS_TO_TALK:
        user_chat = input("Talk!: ")
        print("You said, '{}' That's cool.\n".format(user_chat))

def timer(timeout):
    sleep(timeout)

def main():
    pin = "12345"
    entry = 0
    lockout_time = 10
    incorrect_entries = 0

    while True:
        
        # You know users these days, you can always trust their input!
        entry = getpass(prompt="Enter your 5 digit pin! (00000 to quit): ")

        if entry == EXIT:
            print("Good day!")
            exit(0)

        elif entry == pin:
            #Reset incorrect entries
            incorrect_entries = 0

            chat = multiprocessing.Process(target=chatbot, name="Chat")
            chat.start()
            timeouter = multiprocessing.Process(target=timer, name="Timeouter", args=(TIMEOUT, ))
            timeouter.start()

            while timeouter.is_alive():
                sleep(0.25)

            chat.terminate()

            print("\n!!!!!!Your session has expired!!!!!!")

            

        else:

            incorrect_entries += 1
            
            if incorrect_entries < 3:  
                print("Incorrect entry.  Please try again.")
                print("{0} incorrect entry(ies).  Program will lockout after 3.\n".format(incorrect_entries))
            
            else:
                print("Stop hacking! (For {} seconds)".format(lockout_time))
                sleep(lockout_time)
                lockout_time *= 2
                incorrect_entries = 0

if __name__ == "__main__":
    main()
