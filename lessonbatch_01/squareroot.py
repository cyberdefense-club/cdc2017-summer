import datetime


def sqrt(target, tolerance = 0.00001):
    lo, hi = 0, max(1, target)

    while True:
        mid = lo + (hi - lo)/2
        sq = mid * mid
        if abs(sq-target) < tolerance:
            return mid
        elif sq > target:
            if hi == mid:
                # we are looping, and can't get the precision we want:
                return hi
            else:
                hi = mid
        else:
            if lo == mid:
                # we are looping, and can't get the precision we want:
                return lo
            else:
                lo = mid

    return mid

if __name__ == '__main__':
    f = float(input("For what number do you want the square root? "))
    p = float(input("What precision do you want (must be between 0 and 1)? "))
    t1 = datetime.datetime.now()
    s = sqrt(f, p)
    print(s)
    t2 = datetime.datetime.now()

    print("The square root of {0} is {1} and took {2} to calculate"
          .format(f, s, t2-t1))