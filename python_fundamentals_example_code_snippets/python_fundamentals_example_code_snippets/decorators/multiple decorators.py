class EscapeUnicode:
    def __init__(self,f):
        self.f = f
        self.count = 0
    def __call__(self, *args, **kwargs):
        self.count += 1
        x = self.f(*args,**kwargs)
        return ascii(x)

class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self,f):
        def wrap(*args, **kwargs):
            return f(*args, **kwargs)
        return wrap

trace = Trace()

@trace
@EscapeUnicode
def home(name):
    return "Hello, {}".format(name)



