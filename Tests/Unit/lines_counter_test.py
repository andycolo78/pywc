import unittest

from parameterized import parameterized

from App.Counters.lines_counter import LinesCounter
from App.Counters.counter import Counter


class BytesCounterTest(unittest.TestCase):

    def test_is_implementation_of_counter(self):
        lines_counter = LinesCounter()
        self.assertIsInstance(lines_counter, Counter)

    @parameterized.expand([
        ("test_0", 'xxxx', 0),
        ("test_1", 'xxxxxxxxxx\n', 1),
        ("test_10", 'xx\nxx\nxx\nxx\nxx\nxx\nxx\nxx\nxx\nxx\n', 10)
    ])
    def test_count_lines(self, name, test_chunk, expected_count):
        lines_counter = LinesCounter()
        asserted_count = lines_counter.get_count(test_chunk)

        self.assertEqual(expected_count, asserted_count)
