import sys
from contextlib import contextmanager


@contextmanager
def logging_context_manager():
    #__enter__()
    try:
        yield "value returned by __enter__()" # return value of __enter__()
    #body of with statement executes before __exit__() executes
    #if there is any exception in the body will be caught by the try statement
    #__exit__()
        print("normal __exit__")
    except Exception:
        print("Exceptional Exit __exit__({})".format(sys.exc_info()))