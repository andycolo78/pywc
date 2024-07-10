import sys
from typing import Generator

from App.Readers.reader import Reader


class StdinReader(Reader):

    def read_chunk(self) -> Generator:
        while True:
            chunk = sys.stdin.read(self.CHUNK_SIZE)
            if not chunk:
                break
            yield chunk
