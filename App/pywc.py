"""
Manages pywc business logic
"""


class Pywc:

    def __init__(self):
        self.__filename = ""
        self.__chunk_size = 1024

    def set_file(self, filename: str) -> None:
        self.__filename = filename

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
