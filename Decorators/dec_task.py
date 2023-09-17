def outer(*args,**kwargs):
    def second_outer(func):
        def inner(*dargs,**dkwargs):
            attempts = kwargs['attempts']
            while attempts > 0:
                try:
                    return func(*dargs,**dkwargs)
                except Exception as err:
                    print("Error",err)
                    attempts -= 1
        return inner
    return second_outer

@outer(attempts=5)
def div(a,b):
    return a/b


print(div(1,0))