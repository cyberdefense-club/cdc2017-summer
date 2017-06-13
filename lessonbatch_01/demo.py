import random

target = random.randint(1, 100)

# initialize guess to be something different from target:
guess = -1

while guess != target:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess == target:
        print('You are correct!')
        print('You are really correct!')
        break
    elif guess > target:
        print('Too high!')
        continue
    else:
        print('Too low!')
        continue

    print('Other stuff')

print("Out of the loop.")