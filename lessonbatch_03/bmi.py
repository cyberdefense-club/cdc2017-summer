def convert_feet_to_meters(feet, inches=0):
    # per Google:
    return (feet + inches/12.0) * 0.3048


def convert_pounds_to_kilos(pounds, ounces=0):
    return (pounds + ounces/16.0) / 2.2


def get_int_input(prompt, min_int, max_int):

    while True:
        instring = input(prompt)

        if instring.isdigit():
            intval = int(instring)
            if intval < min_int or intval > max_int:
                print()
                print('Error - please provide an integer between {0} and {1}.'
                      .format(min_int, max_int))
                print()
            else:
                return int(instring)
        else:
            print()
            print('{} is not an integer. Please try again.'.format(instring))
            print()


# Q1:
def calc_bmi_metric(height_meters, weight_kilos):
    return weight_kilos / (height_meters ** 2)


def get_bmi_metric():
    print()
    height_meters = float(input("Enter your height in meters: "))
    weight_kilos = float(input("Enter your weight in kilograms: "))

    return calc_bmi_metric(height_meters, weight_kilos)


# Q2:
def get_bmi_imperial(use_subunits = False):
    print()

    if use_subunits:
        height_subprompt = "feet only"
        weight_subprompt = "pounds only"
    else:
        height_subprompt = weight_subprompt = "decimals allowed"

    height_feet = float(input(f"Enter your height ({height_subprompt}): "))
    if use_subunits:
        height_feet += float(input("Enter your height (inches only): "))/12.0

    if use_subunits:
        print()

    weight_pounds = float(input(f"Enter your weight ({weight_subprompt}): "))
    if use_subunits:
        weight_pounds += float(input("Enter your weight (ounces only): "))/16.0

    return calc_bmi_metric(convert_feet_to_meters(height_feet),
                           convert_pounds_to_kilos(weight_pounds))


# Q3:
# absorbed into the #Q2 code


# Q4:
def get_menu_choice():
    print()
    print("Welcome to the BMI Calculator!")
    print("How would you like to enter your height and weight?")
    print("    1) using meters and kilograms")
    print("    2) using feet only (decimals allowed) and pounds")
    print("    3) using feet and inches for height and pounds and ounces for weight")
    print()
    return get_int_input("    Please enter 1, 2, or 3: ", 1, 3)


def eval_bmi(bmi):

    bmi_category = "obese" if bmi > 30 else \
        "overweight" if bmi >= 25 else \
        "normal" if bmi >= 18.5 else \
        "underweight"

    print(f"Your BMI is: {bmi}")
    print()
    print("BMI is usually categorized as follows:")
    print()
    print("    Below 18.5 == underweight")
    print("    18.5 to 24.9 == normal")
    print("    25.0 to 29.9 == overweight")
    print("    30.0 and above == obese")
    print()
    print(f"As you can see, the BMI we calculated falls into the \"{bmi_category}\" category.")


def main():
    choice = get_menu_choice()

    if choice == 1:
        eval_bmi(get_bmi_metric())
    elif choice == 2:
        eval_bmi(get_bmi_imperial(use_subunits=False))
    else: # choice == 3
        eval_bmi(get_bmi_imperial(use_subunits=True))

    print("Thank you for using the BMI calculator!")


if __name__ == '__main__':
    main()
