import unittest

from sorted_set import SortedSet
from collections.abc import Container, Sized, Iterable, Sequence


class TestConstruction(unittest.TestCase):
    def test_empty(self):
        s = SortedSet()

    def test_sequence(self):
        s = SortedSet([1, 2, 3, 47, 5, 67])

    def test_with_duplicates(self):
        s = SortedSet([1, 22, 3, 3, 4, 4, 55, 55])
        self.assertEqual(s.sequence, [1, 3, 4, 22, 55])

    def test_iterable(self):
        def gen():
            yield 1
            yield 2
            yield 3

        g = gen()
        s = SortedSet(g)


class TestContainer(unittest.TestCase):
    # testing container protocol
    def setUp(self):
        self.s = SortedSet([3, 6, 7, 8])

    def test_positive_containment(self):
        self.assertTrue(3 in self.s)

    def test_negative_containment(self):
        self.assertFalse(2 in self.s)

    def test_positive_non_containment(self):
        self.assertTrue(10 not in self.s)

    def test_negative_non_containment(self):
        self.assertFalse(8 not in self.s)

    def test_container(self):
        self.assertTrue(issubclass(SortedSet, Container))


class TestSized(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(len({}), 0)

    def test_ten(self):
        self.assertEqual(len(SortedSet(range(10))), 10)

    def test_with_duplicates(self):
        self.assertEqual(len(SortedSet([1, 1, 1])), 1)

    def test_sized(self):
        self.assertTrue(issubclass(SortedSet, Sized))


class TestIterable(unittest.TestCase):
    def setUp(self):
        self.s = SortedSet([1, 2, 3, 4, 5])

    def test_iterator(self):
        i = iter(self.s)
        self.assertEqual(next(i), 1)
        self.assertEqual(next(i), 2)
        self.assertEqual(next(i), 3)
        self.assertEqual(next(i), 4)
        self.assertEqual(next(i), 5)
        self.assertRaises(StopIteration, lambda: next(i))

    def test_iterable(self):
        self.assertTrue(issubclass(SortedSet, Iterable))


class TestSequence(unittest.TestCase):
    def setUp(self):
        self.s = SortedSet([1, 2, 3, 4, 5])

    def test_zero(self):
        self.assertEqual(self.s[0], 1)

    def test_at_end(self):
        self.assertEqual(self.s[4], 5)

    def test_beyond_end(self):
        self.assertRaises(IndexError, lambda: self.s[6])

    def test_at_negative_beginning(self):
        self.assertEqual(self.s[-1], 5)

    def test_at_negative_end(self):
        self.assertEqual(self.s[-5], 1)

    def test_beyond_negative_end(self):
        with self.assertRaises(IndexError):
            self.s[-6]

    # Slicing tests
    # the returned sliced object must be sortedset object
    def test_slice_full(self):
        self.assertEqual(self.s[:], SortedSet([1, 2, 3, 4, 5]))

    def test_slice_random(self):
        self.assertEqual((self.s[1:4]), SortedSet([2, 3, 4]))

    def test_slice_till_end(self):
        self.assertEqual(self.s[3:], SortedSet([4, 5]))

    def test_slice_from_beginning(self):
        self.assertEqual(self.s[:3], SortedSet([1, 2, 3]))

    # __reverse__() is required mnormally to perfoem reverse
    # if __reverse__() is not present reverse() still works if __getitem__() and __len__() are present which is true in this case
    # we can also implement __reverse__() in Sorted Set
    def test_reversed(self):
        r = reversed(self.s)
        self.assertEqual(next(r), 5)
        self.assertEqual(next(r), 4)
        self.assertEqual(next(r), 3)
        self.assertEqual(next(r), 2)
        self.assertEqual(next(r), 1)

    # for SortedSet to support index() either it should implement __index__() or it must be a subclass of "Sequence"
    # and it must contain __getitem__() and __len__()
    # "Sequence" is an abstract class in "collections.abc" package which contains mixin methods like index() and count()
    # the implementation of index() in "Sequence" is based on __getitem__() and __len__() methods
    def test_index_positive(self):
        self.assertEqual(self.s.index(2), 1)

    def test_index_negative(self):
        with self.assertRaises(ValueError):
            self.s.index(10)

    def test_sequence(self):
        self.assertTrue(issubclass(SortedSet, Sequence))

    # testing for concatenation
    def test_disjoint_concatenation(self):
        s = SortedSet([1, 2, 3])
        t = SortedSet([4, 5, 6])
        self.assertEqual((s + t), SortedSet([1, 2, 3, 4, 5, 6]))

    def test_self_concatenation(self):
        s = SortedSet([1, 2, 3])
        self.assertEqual((s + s), SortedSet([1, 2, 3]))

    def test_intersection_concatenation(self):
        s = SortedSet([1, 2, 3])
        t = SortedSet([2, 3, 4])
        self.assertEqual((s + t), SortedSet([1, 2, 3, 4]))

    # testing for repetetion
    def test_multiplication(self):
        s = SortedSet([1,2,3])
        self.assertEqual(s*3, s)
    def test_reversed_multiplication(self):
        s= SortedSet([1,2,3])
        self.assertEqual(3*s, s)


class TestEquality(unittest.TestCase):
    def test_equality_of_two_sorted_sets(self):
        self.assertTrue(SortedSet([1, 2, 3]) == SortedSet([1, 2, 3]))

    def test_equality_of_empty(self):
        self.assertTrue(SortedSet() == SortedSet())

    def test_equality_of_itself(self):
        s = SortedSet([1, 2, 3, 4])
        self.assertTrue(s == s)

    def test_type_mismatch(self):
        self.assertFalse(SortedSet([1, 2, 3]) == [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
