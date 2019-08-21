from functools import reduce

# multiple input comprehensions
l = [(x, y) for x in range(10) for y in range(x)]

# values only greater than 2 since resulting expr is evaluated inside second if clause
m = [(x, y) for x in range(10) for y in range(x) if x > 1 if x > 2]

# nested comprehension
lm = [[y * 3 for y in range(x)] for x in range(5)]

# map()
# returns a generator object yielding unicode values for each char in string
mp = map(ord, "This is a string")


# map with multiple input sequences
def combine(x, y, z):
    return "{} {} {}".format(x, y, z)


map_with_multi_inputs = map(combine, ['a', 'b', 'c'], ['p', 'q', 'r'], ['l', 'm', 'n'])

# filter()
# lazy and returns a generator object as map()
f = filter(lambda x: x > 0, [-2, -1, 0, 1, 2])

# reduce()
r = reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])


# Iteration protocols and custom iterators
class CustomIterator:
    def __init__(self, data):
        self._index = 0
        self._data = data

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._data):
            raise StopIteration
        rslt = self._data[self._index]
        self._index += 1
        return rslt


class CustomIterable:
    def __init__(self, data):
        self._data = data

    def __iter__(self):
        return CustomIterator(self._data)
