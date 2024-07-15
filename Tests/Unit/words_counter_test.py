import unittest

from parameterized import parameterized

from App.Counters.words_counter import WordsCounter
from App.Counters.counter import Counter


class WordsCounterTest(unittest.TestCase):

    def test_is_implementation_of_counter(self):
        words_counter = WordsCounter()
        self.assertIsInstance(words_counter, Counter)

    @parameterized.expand([
        ("test_0", 'xxxx', 0),
        ("test_1", 'xxxxxxxxxx\n', 1),
        ("test_10", 'xx\nxx\nxx\nxx\nxx\nxx\nxx\nxx\nxx\nxx\n', 10)
    ])
    def test_count_words(self, name, test_chunk, expected_count):
        words_counter = WordsCounter()
        asserted_count = words_counter.get_count(test_chunk)

        self.assertEqual(expected_count, asserted_count)
