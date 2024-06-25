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

        count_list = []
        for chunk in self.__read_file_by_chunk():
            for idx, counter in enumerate(counters):
                count = counter.get_count(chunk)
                if len(count_list) <= idx:
                    count_list.append(count)
                    continue
                count_list[idx] += count
                idx += idx

        return count_list

    def count_bytes(self) -> int:
        count = 0
        for chunk in self.__read_file_by_chunk():
            count += len(chunk)

        return count

    def count_lines(self) -> int:
        count = 0
        for chunk in self.__read_file_by_chunk():
            count += str(chunk).count('\n')

        count += 1 if not str(chunk).endswith('\n') else 0

        return count

    def __read_file_by_chunk(self) -> bytes:
        with open(self.__filename, 'r') as file:
            while True:
                chunk = file.read(self.__chunk_size)
                if not chunk:
                    break
                yield chunk
