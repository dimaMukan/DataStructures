def fact(val:int):
    if val == 0:
        return 1
    return val * fact(val-1)

print(fact(5))