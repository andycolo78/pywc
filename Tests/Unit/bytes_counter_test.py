import base64
import os
import unittest

from parameterized import parameterized

from App.Counters.bytes_counter import BytesCounter
from App.Counters.counter import Counter


class BytesCounterTest(unittest.TestCase):

    def test_is_implementation_of_counter(self):
        bytes_counter = BytesCounter()
        self.assertIsInstance(bytes_counter, Counter)

    @parameterized.expand([
        ("test_0", 0),
        ("test_1", 1),
        ("test_1000000", 1000000)
    ])
    def test_count_bytes(self, name, chunk_size):
        test_chunk = 'x'*chunk_size
        bytes_counter = BytesCounter()
        bytes_count = bytes_counter.get_count(test_chunk)

        self.assertEqual(chunk_size, bytes_count)
