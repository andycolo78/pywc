import os
import unittest

from parameterized import parameterized

from App.Readers.file_reader import FileReader
from App.Readers.reader import Reader


class FileReaderTest(unittest.TestCase):

    def test_is_implementation_of_reader(self):
        filename = 'test_read.txt'
        file_reader = FileReader(filename)
        self.assertIsInstance(file_reader, Reader)

    @parameterized.expand([
        ("test_c_100", 100),
        ("test_c_1000", 1000),
        ("test_c_1", 1),
        ("test_c_1024", 1024),
        ("test_c_long", 123456789)
    ])
    def test_read_chunk(self, name, file_length):
        filename = 'test_read_chunk.txt'

        with open(filename, 'w') as file:
            file.write('x' * file_length)

        with open(filename, 'r') as file:
            expected_chunk = file.read(1024)

        file_reader = FileReader(filename)
        generator = file_reader.read_chunk()
        chunk = next(generator)

        self.assertEqual(expected_chunk, chunk)

        for chunk in generator:
            pass

        os.remove(filename)
