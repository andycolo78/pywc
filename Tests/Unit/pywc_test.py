import os
import unittest

from parameterized import parameterized

from App.Readers.file_reader import FileReader
from App.pywc import Pywc
from App.Counters.bytes_counter import BytesCounter
from App.Counters.lines_counter import LinesCounter
from App.Counters.words_counter import WordsCounter


class PywcTest(unittest.TestCase):

    def test_set_reader(self):
        filename = 'test_set_reader.txt'

        pywc = Pywc()
        reader = FileReader(filename)
        pywc.set_reader(reader)

        self.assertEqual(reader, pywc._Pywc__reader)

    @parameterized.expand([
        ("test_c_100", 100),
        ("test_c_1000", 1000),
        ("test_c_1", 1),
        ("test_c_1024", 1024),
        ("test_c_long", 123456789)
    ])
    def test_count_bytes(self, name, file_length):
        filename = 'test_count_bytes.txt'

        with open(filename, 'w') as file:
            file.write('x'*file_length)

        pywc = Pywc()
        file_reader = FileReader(filename)
        pywc.set_reader(file_reader)
        bytes_count = pywc.count([BytesCounter()])

        os.remove(filename)

        self.assertEqual(file_length, bytes_count[0])

    @parameterized.expand([
        ("test_l_100", 100),
        ("test_l_1000", 1000),
        ("test_l_1", 1)
    ])
    def test_count_lines(self, name, lines_number):
        filename = 'test_count_lines.txt'

        with open(filename, 'w') as file:
            file.write('zxcvbnmasdfghjklqwertyuiop1234567890\n' * lines_number)

        pywc = Pywc()
        file_reader = FileReader(filename)
        pywc.set_reader(file_reader)
        lines_count = pywc.count([LinesCounter()])

        os.remove(filename)

        self.assertEqual(lines_number, lines_count[0])

    @parameterized.expand([
        ("test_w_100", 100),
        ("test_w_1000", 1000),
        ("test_w_1", 1)
    ])
    def test_count_words(self, name, words_number):
        filename = 'test_count_lines.txt'

        with open(filename, 'w') as file:
            file.write('word ' * words_number)

        pywc = Pywc()
        file_reader = FileReader(filename)
        pywc.set_reader(file_reader)
        words_count = pywc.count([WordsCounter()])

        os.remove(filename)

        self.assertEqual(words_number, words_count[0])

    def test_count_lines_non_terminated(self):
        filename = 'test_count_lines_non_terminated.txt'

        with open(filename, 'w') as file:
            file.write('xxxxxxxxxx\nyyyyyyyyy')

        pywc = Pywc()
        file_reader = FileReader(filename)
        pywc.set_reader(file_reader)
        lines_count = pywc.count([LinesCounter()])

        os.remove(filename)

        self.assertEqual(2, lines_count[0])

