from App.Counters.counter import Counter
from App.Readers.reader import Reader

"""
Manages pywc business logic
"""


class Pywc:

    def __init__(self):
        self.__reader = None
        self.__chunk_size = 1024

    def set_reader(self, reader: Reader) -> None:
        self.__reader = reader

    def count(self, counters: list):
        for counter in counters:
            if not isinstance(counter, Counter):
                raise TypeError('Only Counter subclasses objects are allowed')

        count_list = [0] * len(counters)
        last_chunk = ''
        for chunk in self.__reader.read_chunk():
            for idx, counter in enumerate(counters):
                count_list[idx] += counter.get_count(chunk)
            last_chunk = chunk

        for idx, counter in enumerate(counters):
            count_list[idx] += 1 if counter.should_count_last(last_chunk) else 0

        return count_list
