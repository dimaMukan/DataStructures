def dec_param(*args,**kwargs):
    def dec(func):
        def function(*dargs,**dkwargs):
            attempts = kwargs['attempts']
            while attempts > 0:
                try:
                    return func(*dargs,**dkwargs)
                except Exception as err:
                    print(f"Error: {err}, attempts {attempts}")
                    attempts -= 1
        return function
    return dec

def simple_dec(func):
    def function(*args,**kwargs):
        print("Second Decorator")
        return func(*args,**kwargs)
    return function



@dec_param(attempts=5)
@simple_dec
def div(a,b):
    return a/b

print(div(1,0))