# fibonacci


def fib(n):
    # fib(n) = 1, if n in (1, 2)
    # else: fib(n) = fib(n-1) + fib(n-2)

    if n == 1 or n == 2:
        return 1
    else:
        x = fib(n-1)
        y = fib(n-2)
        return x + y

nth = int(input("Which fibonacci number shall we calculate? "))
print("Fibonacci number {0} is {1}.".format(nth, fib(nth)))