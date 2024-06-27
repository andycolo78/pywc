from App.Counters.counter import Counter

"""
Manages pywc business logic
"""


class Pywc:

    def __init__(self):
        self.__filename = ""
        self.__chunk_size = 1024

    def set_file(self, filename: str) -> None:
        self.__filename = filename

    def count(self, counters: list):
        for counter in counters:
            if not isinstance(counter, Counter):
                raise TypeError('Only Counter subclasses objects are allowed')

        count_list = [0] * len(counters)
        last_chunk = ''
        for chunk in self.__read_file_by_chunk():
            for idx, counter in enumerate(counters):
                count_list[idx] += counter.get_count(chunk)
            last_chunk = chunk

        for idx, counter in enumerate(counters):
            count_list[idx] += 1 if counter.should_count_last(last_chunk) else 0

        return count_list

    def __read_file_by_chunk(self) -> bytes:
        with open(self.__filename, 'r') as file:
            while True:
                chunk = file.read(self.__chunk_size)
                if not chunk:
                    break
                yield chunk
