fibDict = {1 : 1, 2 : 1 }

def fibonacci(n):
    if n not in fibDict: 
        fibDict[n] = fibonacci(n-1) + fibonacci(n-2)
    
    return fibDict[n]

print(fibonacci(int(input("Enter an illustrious number to be Fibbonaccied: "))))
