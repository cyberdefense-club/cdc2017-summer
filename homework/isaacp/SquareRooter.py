import sys
numberToSquareRoot = float(input("Give me a number to take the square root of: "))
squareRootNumber = 0.0
squaredNumber = 0.0
if numberToSquareRoot == 0:
    print("Cannot take a square root of 0")
    sys.exit()
squareRootNumber += 0.0000001
if numberToSquareRoot == int(numberToSquareRoot):
    for anotherSquaredNumber in range(1, int(numberToSquareRoot)):
        squaredNumber = anotherSquaredNumber * anotherSquaredNumber
        if squaredNumber == numberToSquareRoot:
            print(anotherSquaredNumber)
            sys.exit()
while True:
    squaredNumber = squareRootNumber * squareRootNumber
    if squaredNumber > numberToSquareRoot - 0.00001 and squaredNumber < numberToSquareRoot + 0.00001:
        print(squareRootNumber)
        sys.exit()
    else:
        squareRootNumber += 0.0000001