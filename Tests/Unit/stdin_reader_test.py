import io
import os
import sys
import unittest

from parameterized import parameterized

from App.Readers.stdin_reader import StdinReader
from App.Readers.reader import Reader


class StdinReaderTest(unittest.TestCase):

    def test_is_implementation_of_reader(self):
        stdin_reader = StdinReader()
        self.assertIsInstance(stdin_reader, Reader)

    @parameterized.expand([
        ("test_c_100", 100),
        ("test_c_1000", 1000),
        ("test_c_1", 1),
        ("test_c_1024", 1024),
        ("test_c_long", 123456789)
    ])
    def test_read_chunk(self, name, stream_length):
        stream_string = 'x' * stream_length
        expected_chunk = stream_string[:1024]

        sys.stdin = io.StringIO(stream_string)

        stdin_reader = StdinReader()
        generator = stdin_reader.read_chunk()
        chunk = next(generator)

        self.assertEqual(expected_chunk, chunk)
