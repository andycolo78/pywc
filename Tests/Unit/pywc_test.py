import os
import unittest

from parameterized import parameterized

from App.pywc import Pywc
from App.Counters.bytes_counter import BytesCounter


class PywcTest(unittest.TestCase):

    def test_set_file(self):
        filename = 'test_set_file.txt'
        file_length = 100

        with open(filename, 'w') as file:
            file.write('x'*file_length)

        pywc = Pywc()
        pywc.set_file(filename)

        os.remove(filename)

        self.assertEqual(filename, pywc._Pywc__filename)

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
        pywc.set_file(filename)
        bytes_counter = BytesCounter()
        bytes_count = pywc.count([bytes_counter])

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
        pywc.set_file(filename)
        lines_count = pywc.count_lines()

        os.remove(filename)

        self.assertEqual(lines_number, lines_count)

    def test_count_lines_non_terminated(self):
        filename = 'test_count_lines_non_terminated.txt'

        with open(filename, 'w') as file:
            file.write('xxxxxxxxxx\nyyyyyyyyy')

        pywc = Pywc()
        pywc.set_file(filename)
        lines_count = pywc.count_lines()

        os.remove(filename)

        self.assertEqual(2, lines_count)

