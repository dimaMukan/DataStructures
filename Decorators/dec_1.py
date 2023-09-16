def outer():
    def div(a,b):
        return a/b
    return div



var = outer()
print(type(var))
print(var(1,2))