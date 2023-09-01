import math

def sum_func(n):
    if n < 1:
        return 0

    return n%10 + sum_func(math.trunc(n/10))

print(sum_func(1234))

