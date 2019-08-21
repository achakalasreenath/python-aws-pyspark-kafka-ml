def check_non_negative(index):
    def validator(f):
        def wrap(*args,**kwargs):
            if args[index] < 0:
                raise ValueError("argument is negative")
            return f(*args)
        return wrap
    return validator

@check_non_negative(1)
def home(length,size):
    print(length,size)