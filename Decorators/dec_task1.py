def dec_par(*args,**kwargs):            # Param for decoration
    def dec(func):                      # Decorator
        def function(*dargs,**dkwargs): # Realisation of Function
            print(*args,**kwargs)
            return func(*dargs,**dkwargs)
        return function
    return dec


@dec_par("Par for decorator")
def div(a,b):
    return a/b

print(div(1,1))