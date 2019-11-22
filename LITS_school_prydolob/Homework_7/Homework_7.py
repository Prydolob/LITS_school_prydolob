# class ValuerangeError(Exception):
#     def __init__(self, mes):
#         self.mes = mes


class Range:
    """
    Iterable class
    """

    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return RangeIterator(self.start, self.stop, self.step)


class RangeIterator:
    """
    Iterator class
    """

    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __next__(self):
        if self.start < self.stop:
            tmp = self.start
            if self.step > 0:
                self.start += self.step
            elif self.step == 0:
                raise StopIteration
                # raise ValuerangeError("Can't be zero!")
            elif self.step < 0:
                raise StopIteration
            return tmp
        elif self.start > self.stop:
            tmp = self.start
            if self.step < 0:
                self.start -= self.step
            elif self.step == 0:
                raise StopIteration
                # raise ValuerangeError("Can't be zero!")
            elif self.step > 0:
                raise StopIteration
            return tmp
        raise StopIteration

    def __iter__(self):
        return self


a = RangeIterator(10, 2, -2)

for i in a:
    print(i)
