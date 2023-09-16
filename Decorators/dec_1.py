def second_outer(par):
    def outer(func):
        def inner(*args, **kwargs):
            print(par)
            return func(*args, **kwargs)
        return inner
    return outer

def sum(a,b,c):
    return a+b+c

@second_outer("Message before")
def div(a,b):
    return a/b

print(div(1,2))