

def par_dec(*args,**kwargs):
    def deco(my_class):
        def inner(*dargs,**dkwargs):
            password = 'secret_password'
            if kwargs['password'] != password:
                raise ValueError("You cant do a class object, Authorization Error")
            else:
                print("Object is done")
            return my_class(*dargs,**dkwargs)
        return inner
    return deco

password = 'secret_password'


# @par_dec(password='my_password')
@par_dec(password='secret_password')
class My_class():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'a: {self.a}, b: {self.b}'



a = My_class(1,2)
print(a)

