import traceback


class InclinationError(Exception):
    pass


def inclination(x, y):
    try:
        result = y / x
    except ZeroDivisionError as e:
        raise InclinationError("slope is not defined for x") from e


def main():
    try:
        inclination(0, 2)
    except InclinationError as e:
        print(e.__cause__)
        traceback.print_tb(e.__traceback__)
        s = traceback.format_tb(e.__traceback__)
        print(s)


if __name__ == "__main__":
    main()
    print("finished")
