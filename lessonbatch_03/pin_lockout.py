from getpass import getpass
import time
import multiprocessing
import sys


OS_Class = None
try:
    import msvcrt
    OS_Class = "Windows"
except ImportError:
    import sys, termios
    OS_Class = "Unix"


def flush_input():
    if OS_Class == "Windows":
        while msvcrt.kbhit():
            msvcrt.getch()
    elif OS_Class == "Unix":
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)


def chat():
    sys.stdout = open(1, 'w')
    sys.stdin = open(0, 'r')

    print("\nHello, and welcome. Talk to me!\n(Enter 00000 at any time to quit.)")
    while True:
        try:
            text_in = input("\nSay something! ")
        except KeyboardInterrupt:
            text_in = "00000"

        if text_in == "00000":
            print("\nThanks for stopping by. Talk to you later!")
            exit(0)
        else:
            print(f"You said: '{text_in}'!")


def timer(seconds):
    time.sleep(seconds)


def main():

    secret = "12345"
    timeout = 3

    try:
        while True:
            failures = 0
            pin = ""
            while pin != secret:
                flush_input()
                pin = getpass("\n\nPlease enter your 5-digit pin (enter 00000 to quit): ")
                if pin == "00000":
                    print("\nThank you for using ChatBot. Come back soon!\n")
                    return
                elif pin == secret:
                    try:
                        failures = 0
                        print("You have entered the correct pin. Thank you.")
                        chatbot = multiprocessing.Process(target=chat, name="ChatBot")
                        chatbot.start()
                        clock = multiprocessing.Process(target=timer, name="Timer", args=(15, ))
                        clock.start()

                        while chatbot.is_alive() and clock.is_alive():
                            time.sleep(0.25)

                        if clock.is_alive():
                            clock.terminate()
                        else:
                            print("\n***** Your session has expired. *****\n")

                        if chatbot.is_alive():
                            chatbot.terminate()

                    except KeyboardInterrupt:
                        print("Ending program due to keyboard interrupt.")
                        exit(0)
                else:
                    failures += 1
                    if failures % 3 == 0:
                        print(f"Third failure. Locking program for {timeout} seconds.")
                        time.sleep(timeout)
                        timeout *= 2
                    else:
                        print(f"Failure number {failures}. The screen will lock after every 3 failures.")

    except KeyboardInterrupt:
        print("\nExiting program due to user request (keyboard interrupt).\n")
        exit(0)

if __name__ == '__main__':
    main()
