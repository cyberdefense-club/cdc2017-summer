import getpass
import time

attempts = 0
sleep = 10
pin = '12345'


def login(pin):
    attempt = getpass.getpass("Please enter your PIN: ")
    if attempt == pin:
        return True
    else:
        return False

t = time.time()

if login(pin):
    print("You have logged in!")
    print("What would you like to say to our top-secret chatbot?")
    while (1):
        response = input("Say something:")
        response = "[chatbot]You said: " + response
        print(response)
        if time.time() - t == 600:
            if login(pin):
                print("You have logged in again")
                t = time.time()
            else:
                print("No more chatbot for you, young man.")
                break
else:
    attempts += 1
    if attempts == 3:
        time.sleep(sleep)
        sleep *= 2
