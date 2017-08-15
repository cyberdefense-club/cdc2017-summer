FOOT_TO_METER = 0.3048
POUND_TO_KILOGRAM = 0.453592

def calc_bmi(height_m, wheight_kg):
    return weight_kg / (height**2)

def imperial_to_metric(feet, pounds):
    return (FOOT_TO_METER * feet, POUND_TO_KILOGRAM * pounds)

mode = input("1. Metric\n2. Imperial (decimals)\n3. Imperial\n")

#Metric
if mode == "1":
    height_m = float(input("Enter your height in meters: "))
    weight_kg = float(input("Enter your weight in kilograms: "))

#Imperial
elif mode == "2" or mode == "3":
    height_ft = float(input("Enter your height in feet: "))
    if mode == "3": height_ft += float(input("Inches: ")) / 12.0

    weight_lb = float(input("Enter you wieght in pounds: ")) 
    if mode == "3": weight lb += float(input("Ounces")) / 16.0

bmi = calc_bmi(height_m, weight_kg)

print("Your Body Mass Index is:", bmi)