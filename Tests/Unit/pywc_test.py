import os
import unittest
from io import StringIO
from unittest.mock import MagicMock, patch

from Utils.pywc import Pywc


class PywcTest(unittest.TestCase):

    def test_set_file(self):
        filename = 'test_c_option_10.txt'
        file_length = 100

        with open(filename, 'w') as file:
            file.write('x'*file_length)

        pywc = Pywc()
        pywc.set_file(filename)

        self.assertEqual(filename, pywc._Pywc__filename)

    def test_count_bytes(self):
        filename = 'test_c_option_10.txt'
        file_length = 100

        with open(filename, 'w') as file:
            file.write('x'*file_length)

        pywc = Pywc()
        pywc.set_file(filename)
        bytes_count = pywc.count_bytes()

        self.assertEqual(file_length, bytes_count)

        os.remove(filename)

    def test_count_bytes_100M(self):
        filename = 'test_c_option_10.txt'
        file_length = 100000000

        with open(filename, 'w') as file:
            file.write('x'*file_length)

        pywc = Pywc()
        pywc.set_file(filename)
        bytes_count = pywc.count_bytes()

        self.assertEqual(file_length, bytes_count)

        os.remove(filename)

