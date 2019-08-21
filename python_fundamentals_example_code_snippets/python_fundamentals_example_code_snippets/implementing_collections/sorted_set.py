from bisect import bisect_left
from collections.abc import Sequence
# Extending from Sequnece to provide index() based on __getitem__() and __len__()
from itertools import chain


class SortedSet(Sequence):
    def __init__(self, sequence=[]):
        self.sequence = sorted(set(sequence))

    def is_unique_and_sorted(self):
        """checks if the items in the sorted set are unoque and the sequence is sorted"""
        return all((self(i) < self(i+1) for i in range(len(self)-1))) # all() returns true if all the items in the iterable are TRUE

    def __contains__(self, item):
        """a collection implements container protocol if it implements __conatins__()
            when an "in" or a "not in " is used on a collection then __contains__() is called on that collection
            which internally iterates over each element to find a match
            so the sequence must be an iterable"""
        index = bisect_left(self.sequence, item)
        if (len(self.sequence) != index) and (self.sequence[index] == item):
            return True
        return False

    def __len__(self):
        """ a collection implements sized protocol if it implements __len__()
     len(collection) calls __len__() of that collection"""
        return len(self.sequence)

    def __iter__(self):
        """iteration protocol"""
        for item in self.sequence:
            yield item

    def __getitem__(self, index):
        """Sequence protocol implements __getitem__()
        used for indexing, slicing, reversing,count() etc
        __getitem__() also implements iterator protocol if the object supports indexing
        the value of the index will be of type "slice" if slicing is called upon SortedSet"""
        result = self.sequence[index]
        return SortedSet(result) if isinstance(index, slice) else result

    def __eq__(self, other):
        if not isinstance(other, SortedSet):
            return NotImplemented
        return self.sequence == other.sequence

    def __ne__(self, other):
        if not isinstance(other, SortedSet):
            return NotImplemented
        return self.sequence != other.sequence

    def index(self, item):
        assert self.is_unique_and_sorted(),"Items are not sorted" #Class invariant assert that can be used for all the class methods
        index = bisect_left(self.sequence, item)
        if ((index != len(self.sequence)) and (self.sequence[index] == item)):
            return index
        raise ValueError("Item not found")

    def count(self, item):
        assert self.is_unique_and_sorted(), "Items are not sorted"
        return int(self.__contains__(item))

    def __add__(self, rhs):
        return SortedSet(chain(self.sequence, rhs.sequence))

    # invoked when '*' is used with SortedSet instance on the left hand side of '*'
    def __mul__(self, rhs):
        return self if rhs > 0 else SortedSet()

    # invoked when '*' is used with SortedSet instance on the right hand side of '*'
    # reversed mul
    def __rmul__(self, lhs):
        return self * lhs  # invokes __mul__()

    def __str__(self):
        return "{}".format(self.sequence)

    def __repr__(self):
        return "{}".format(self.sequence)
