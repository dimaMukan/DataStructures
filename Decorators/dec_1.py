def outer(func):
    def inner(*args, **kwargs):
        print('try')
        return func(*args, **kwargs)

    return inner

def sum(a,b,c):
    return a+b+c

def div(a,b):
    return a/b


var = outer(div)
var1 = outer(sum)
print(type(var))
print(var(1,2))
print(var1(1,2,3))