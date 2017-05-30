# fibonacci

listMain = [0, 0, 1]
charIn = int(input("How many numbers do you want me to give you, integer number please: "))
for x in range(charIn - 1):
    listMain[0] = listMain[1]
    listMain[1] = listMain[2]
    output = listMain[0] + listMain[1]
    listMain[2] = output

print(listMain[2])

# square root

