#decorator class to determine the no of time the function has been called
class CallCount:
    def __init__(self,f):
        self.f = f
        self.count = 0

    def __call__(self,*args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)


@CallCount
def hello(name):
    return "Hello, {}".format(name)
