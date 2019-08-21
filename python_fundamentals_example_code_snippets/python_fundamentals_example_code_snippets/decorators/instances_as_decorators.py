import functools
class Trace():
    def __init__(self):
        self.enabled = True

    def __call__(self,f):
        @functools.wraps(f)
        def wrap(*args, **kwargs):
            if self.enabled is True:
                print("Calling {}".format(f))
            return f(*args, **kwargs)
        return wrap

trace = Trace()

@trace
def rotate_list(l):
    l.append(l[0])
    del l[0]
    return l