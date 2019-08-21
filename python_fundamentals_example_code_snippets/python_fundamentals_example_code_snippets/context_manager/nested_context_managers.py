from contextlib import contextmanager

@contextmanager
def nest_test(x):
    print("Entering nest_test {}".format(x))
    yield x
    print("exiting nest_test {}".format(x))

def main():
    with nest_test("outer") as n1, nest_test("inner in {}".format(n1)) as n2:
        print("body")
if __name__ == "__main__":
    main()