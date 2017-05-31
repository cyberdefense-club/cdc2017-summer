#!/usr/bin/python3
import datetime
import sys
sys.setrecursionlimit(10**8)


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


@memoize
def memfib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return memfib(n-1) + memfib(n-2)


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_pri = 0
        fib_cur = 1
        cur = 1
        while cur <= n:
            fib_pri, fib_cur = fib_cur, fib_cur + fib_pri
            cur += 1
        return fib_pri


if __name__ == '__main__':

    n = int(input("What fibonacci number would you like for memfib(n)? "))
    t1 = datetime.datetime.now()
    f = memfib(n)
    t2 = datetime.datetime.now()
    print("Fibonacci number {0} is {1}.".format(n, f))
    print("This number has length {0} and took {1} to calculate."
          .format(len(str(f)), str(t2-t1)))

    n = int(input("What fibonacci number would you like for fib(n)? "))
    t1 = datetime.datetime.now()
    f = fib(n)
    t2 = datetime.datetime.now()
    print("Fibonacci number {0} is {1}.".format(n, f))
    print("This number has length {0} and took {1} to calculate."
          .format(len(str(f)), str(t2-t1)))
