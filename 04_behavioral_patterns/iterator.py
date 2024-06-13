"""
The Iterator pattern is a design pattern that provides a way to access the elements of an aggregate object sequentially
without exposing its underlying representation. In Python, this is typically implemented using the __iter__ and
__next__ methods.
"""


class MyIterator:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        self._current = 0
        return self

    def __next__(self):
        if self._current >= len(self.data):
            raise StopIteration
        result = self.data[self._current]
        self._current += 1
        return result