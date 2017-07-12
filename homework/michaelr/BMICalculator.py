print("Welcome to the BMI Calculator!")
print("How would you like to enter your height and weight?")
print("\n    ")
print("1) using meters and kilograms")
print("2) using feet only (decimals allowed) and pounds")
print("3) using feet and inches for height and pounds and ounces for weight")

def calcBMI(weight, height, metric):

    if metric:
        return weight / height ** 2
    else:
        height = height / 0.3048
        weight = weight / 0.453592
        return weight / height ** 2
mode = int(input("Please enter 1, 2, or 3. . ."))

if mode == 1:
    h = float(input("What is your height in meters?"))
    w = float(input("What is your weight in kilograms?"))

    print("Your BMI is: " + str(calcBMI(w, h, True)))
if mode == 2:
    h = float(input("Height in feet ?"))
    w = float(input("Weight in pounds? "))

    print("Your BMI is: " + str(calcBMI(h, w, False)))
if mode == 3:
    h = float(input("Height in feet? (no inches): "))
    h += float(input("Height in inches? "))/12
    w = float(input("Weight in pounds? "))
    w += float(input("Weight in ounces? "))/16

    print("Your BMI is: " + str(calcBMI(h, w, False)))
if mode < 0 and mode > 3:
    print("Number not between 1 and 3, exiting program. . .")
