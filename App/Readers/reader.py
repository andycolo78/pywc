from typing import Generator


class Reader:

    CHUNK_SIZE = 1024

    def __init__(self, source):
        self.source = source

    def read_chunk(self) -> Generator:
        """ chunk generator from stream"""
        pass
