import io
import math
import sys

class NewChainedError(Exception):
    pass

class TriangleError(Exception):
    def __init__(self, text, sides):
        super().__init__(text)
        self._sides = sides

    def __str__(self):
        return "{} for sides {}".format(self.args[0], self._sides)

    def __repr__(self):
        return "Triangle Error: {!r} for sides {!r}".format(self.args[0], self._sides)


def triangle_area(a, b, c):
    sorted_sides = sorted((a, b, c))
    if sorted_sides[2] > sorted_sides[0] + sorted_sides[1]:
        raise TriangleError("Illegal Triangle", sorted_sides)
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def main():
    try:
        a= triangle_area(1, 2, 5)
        print(a)
    except TriangleError as e:
        try:
            raise ValueError("Second Exception")
        except ValueError as e1:
            print("printing context..")
            print(e1.__context__)

if __name__ == "__main__":
    main()