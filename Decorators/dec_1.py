def second_outer(*bargs,**bkwargs):
    def outer(func):
        def inner(*args, **kwargs):
            print(*bargs,**bkwargs)
            return func(*args, **kwargs)
        return inner
    return outer

def sum(a,b,c):
    return a+b+c

@second_outer("Message before")
def div(a,b):
    return a/b

print(div(1,2))