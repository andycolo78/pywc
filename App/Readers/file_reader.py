from typing import Generator

from App.Readers.reader import Reader


class FileReader(Reader):

    def __init__(self, source):
        super().__init__(source)

    def read_chunk(self) -> Generator:
        with open(self.source, 'r') as file:
            while True:
                chunk = file.read(Reader.CHUNK_SIZE)
                if not chunk:
                    break
                yield chunk
