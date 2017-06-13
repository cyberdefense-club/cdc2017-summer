# fibonacci

# isaac:
listMain = [0, 0, 1]
charIn = int(input("How many numbers do you want me to give you, integer number please: "))
for x in range(charIn - 1):
    listMain[0] = listMain[1]
    listMain[1] = listMain[2]
    output = listMain[0] + listMain[1]
    listMain[2] = output

print(listMain[2])

# nick:
high = 1
low = 0
mid = 0
current = 0
target = input("Type a whole number for Fibonacci that is higher than 0: ")
while int(target) < 1:
    target = input("Type a whole number for Fibonacci that is higher than 0: ")
while current < int(target):
    if int(current) == 0:
        print (str(high))
    else:
        mid = high
        high = high + low
        low = mid
        print (str(high))
    current += 1


# keenan:
def fcalc(m):
    fnumbers=[1, 1]
    output=2
    if m==1 or m==2:
        return str(1)
    else:
        counter = 3

    while counter < m:
        fnumbers.append(output)
        output += fnumbers[-2]
        counter +=1
        del fnumbers[-3]

    return output

print("Fibonacci calculator")
place=int(input("Which Fibonacci number? : "))
print(fcalc(place))


# square root

