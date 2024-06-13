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

    def __read_file_by_chunk(self) -> bytes:
        with open(self.__filename, 'rb') as file:
            while True:
                chunk = file.read(self.__chunk_size)
                if not chunk:
                    break
                yield chunk
