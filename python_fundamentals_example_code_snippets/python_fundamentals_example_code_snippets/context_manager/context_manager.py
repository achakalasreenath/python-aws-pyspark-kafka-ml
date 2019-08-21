class LoggingContextManager:
    def __enter__(self):
        return "value returned by __enter__()"

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("__exit__({},{},{}):Normally Terminated".format(exc_type,exc_val,exc_tb))
        elif exc_type is not None:
            print( "__exit__({},{},{}):Exceptionally Terminated".format(exc_type,exc_val,exc_tb))
