class SimpleList:
    def __init__(self, list):
        self._list = list

    def __getitem__(self, item):
        return self._list[item]

    def sort(self):
        return self._list.sort()

    def add(self, item):
        self._list.add(item)

    def __len__(self):
        return len(self._list)

    def __str__(self):
        return "{}".format(self._list)

    def __repr__(self):
        return "SimpleList : {}".format(self._list)


class SortedList(SimpleList):
    def __init__(self, list):
        super().__init__(list)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()

    def __str__(self):
        return "{}".format(self._list)

    def __repr__(self):
        return "Sortedlist: {}".format(self._list)


class IntList(SimpleList):
    def __init__(self, list):
        self.validate()
        super().__init__(list)

    def validate(self):
        for x in self._list:
            if not isinstance(x, int):
                raise ValueError("{} is not an integer".format(x))

    def __str__(self):
        return "{}".format(self._list)

    def __repr__(self):
        return "IntList: {}".format(self._list)


class SortedIntList(SortedList, IntList):
    def __repr__(self):
        return "SortedIntList : {}".format(list(self))
