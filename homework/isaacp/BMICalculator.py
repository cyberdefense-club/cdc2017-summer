def convert_feet_to_meters(height):
    return height * 12 * 2.54 / 100


def convert_pounds_to_kilograms(weight):
    return weight / 2.2222


def calculate_bmi(height, weight):
    return weight / (height ** 2)


def calculate_feet_from_multi(feet, inches):
    return feet + (inches / 12)


def calculate_pounds_from_multi(pounds, ounces):
    return pounds + (ounces / 16)


def type_checker(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"


def main():
    print("Endings for your height/weight are: ft, m, ft,in and kg, lb, lb,oz")
    print("Example for ft,in and lb,oz: 5,10ft,in  200,10lb,oz")
    isNotFinished = True
    while isNotFinished:
        heightStr = input("Give me your height in feet or meters: ")
        if heightStr[-2:] == "ft":
            try:
                height = float(heightStr[:-2])
                isHeightMetric = False
                isNotFinished = False
            except ValueError:
                print("Inputted value is not a floating point number.")
        elif heightStr[-1:] == "m":
            try:
                height = float(heightStr[:-1])
                isHeightMetric = True
                isNotFinished = False
            except ValueError:
                print("Inputted value is not a floating point number.")
        elif heightStr[-5:] == "ft,in":
            heightInStr = ""
            for charFt in heightStr[0:-5]:
                if charFt == ",":
                    heightFtStr = heightInStr
                    del heightInStr
                    heightInStr = ""
                else:
                    heightInStr = heightInStr + charFt
            try:
                heightFt = int(heightFtStr)
                heightIn = int(heightInStr)
                isHeightMetric = False
                isNotFinished = False
                height = calculate_feet_from_multi(heightFt, heightIn)
            except ValueError:
                print("Inputted value is not a floating point number.")
        else:
            print("Inputted value cannot be used.")
    isNotFinished = True
    while isNotFinished:
        weightStr = input("Give me your weight in pounds or kilograms: ")
        if weightStr[-2:] == "lb":
            try:
                weight = float(weightStr[:-2])
                isWeightMetric = False
                isNotFinished = False
            except ValueError:
                print("Inputted value is not a floating point number.")
        elif weightStr[-2:] == "kg":
            try:
                weight = float(weightStr[:-2])
                isWeightMetric = True
                isNotFinished = False
            except ValueError:
                print("Inputted value is not a floating point number.")
        elif weightStr[-5:] == "lb,oz":
            weightOzStr = ""
            for charLb in weightStr[0:-5]:
                if charLb == ",":
                    weightLbStr = weightOzStr
                    del weightOzStr
                    weightOzStr = ""
                else:
                    weightOzStr = weightOzStr + charLb
            try:
                heightLb = int(weightLbStr)
                heightOz = int(weightOzStr)
                isWeightMetric = False
                isNotFinished = False
                weight = calculate_pounds_from_multi(heightLb, heightOz)
            except ValueError:
                print("Inputted value is not a floating point number.")
        else:
            print("Inputted value cannot be used.")
    if not isHeightMetric:
        height = convert_feet_to_meters(height)
    if not isWeightMetric:
        weight = convert_pounds_to_kilograms(weight)
    bmi = calculate_bmi(height, weight)
    print(str(bmi))
    print(type_checker(bmi))

if __name__ == '__main__':
    main()
