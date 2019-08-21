from contextlib import contextmanager


@contextmanager
def propagator(name, propagate):
    try:
        yield name
        print(name, "Exited normally")
    except:
        print(name,"received exception")
        if propagate:
            raise ValueError("Error")

def main():
    with propagator("outer",True) as p1, propagator("inner", True) as n2:
        raise ValueError("Body Error")

if __name__ == "__main__":
    main()