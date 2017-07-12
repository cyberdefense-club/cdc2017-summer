listMain = [0, 1]
charIn = int(input("How many numbers do you want me to give you, integer number please: "))
print(str(listMain[1]))
for x in range(charIn - 1):
    #this will output the fibonacci sequence
    output = listMain[x] + listMain[x+1]
    listMain.append(output)
    print(str(output))