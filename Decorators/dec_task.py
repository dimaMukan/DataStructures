def outer(*args,**kwargs):
    def second_outer(func):
        def inner(*dargs,**dkwargs):
            attempts = kwargs['attempts']
            while attempts > 0:
                try:
                    return func(*dargs,**dkwargs)
                except Exception as err:
                    print(f"Error: {err}, attempts: {attempts}")
                    attempts -= 1
        return inner
    return second_outer

@outer(attempts=50)
def div(a,b):
    return a/b


print(div(1,0))