import io
import os
import sys
import unittest
from io import StringIO
from unittest.mock import MagicMock, patch

from pywc import main


class MainTest(unittest.TestCase):

    def test_main_calls_pywc(self):
        filename = 'test_c_option_10.txt'
        file_length = 100

        with open(filename, 'w') as file:
            file.write('x'*file_length)

        options = ['pywc.py', '-c', filename]

        mocked_pywc = MagicMock()

        main(options, mocked_pywc)

        mocked_pywc.set_reader.assert_called()
        mocked_pywc.count.assert_called()

        os.remove(filename)

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_c_option(self, stdout):

        filename = 'test_c_option_1M.txt'
        file_length = 1000000

        with open(filename, 'w') as file:
            file.write('x' * file_length)

        options = ['pywc.py', '-c', filename]

        mocked_pywc = MagicMock()
        mocked_pywc.count.return_value = [file_length]

        main(options, mocked_pywc)

        printed_message = stdout.getvalue().strip()

        self.assertEqual(f"{file_length} bytes {filename}", printed_message)

        os.remove(filename)

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_c_option_1(self, stdout):

        filename = 'test_c_option_1.txt'
        file_length = 1

        with open(filename, 'w') as file:
            file.write('x' * file_length)

        options = ['pywc.py', '-c', filename]

        mocked_pywc = MagicMock()
        mocked_pywc.count.return_value = [file_length]

        main(options, mocked_pywc)

        printed_message = stdout.getvalue().strip()

        self.assertEqual(f"{file_length} byte {filename}", printed_message)

        os.remove(filename)

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_l_option(self, stdout):

        filename = 'test_l_option_1000.txt'
        lines_number = 1000

        with open(filename, 'w') as file:
            file.write('zxcvbnmasdfghjklqwertyuiop1234567890\n' * lines_number)

        options = ['pywc.py', '-l', filename]

        mocked_pywc = MagicMock()
        mocked_pywc.count.return_value = [lines_number]

        main(options, mocked_pywc)

        printed_message = stdout.getvalue().strip()

        self.assertEqual(f"{lines_number} lines {filename}", printed_message)

        os.remove(filename)

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_l_option_1(self, stdout):

        filename = 'test_l_option_1.txt'
        lines_number = 1

        with open(filename, 'w') as file:
            file.write('zxcvbnmasdfghjklqwertyuiop1234567890\n' * lines_number)

        options = ['pywc.py', '-l', filename]

        mocked_pywc = MagicMock()
        mocked_pywc.count.return_value = [lines_number]

        main(options, mocked_pywc)

        printed_message = stdout.getvalue().strip()

        self.assertEqual(f"{lines_number} line {filename}", printed_message)

        os.remove(filename)

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_w_option(self, stdout):

        filename = 'test_w_option_1000.txt'
        word_number = 1000

        with open(filename, 'w') as file:
            file.write('word ' * word_number)

        options = ['pywc.py', '-w', filename]

        mocked_pywc = MagicMock()
        mocked_pywc.count.return_value = [word_number]

        main(options, mocked_pywc)

        printed_message = stdout.getvalue().strip()

        self.assertEqual(f"{word_number} words {filename}", printed_message)

        os.remove(filename)

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_w_option_1(self, stdout):

        filename = 'test_w_option_1000.txt'
        word_number = 1

        with open(filename, 'w') as file:
            file.write('word ' * word_number)

        options = ['pywc.py', '-w', filename]

        mocked_pywc = MagicMock()
        mocked_pywc.count.return_value = [word_number]

        main(options, mocked_pywc)

        printed_message = stdout.getvalue().strip()

        self.assertEqual(f"{word_number} word {filename}", printed_message)

        os.remove(filename)

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_wrong_option(self, stdout):
        filename = 'test_c_option_10.txt'
        file_length = 100

        with open(filename, 'w') as file:
            file.write('x' * file_length)

        options = ['pywc.py', '-x', filename]

        mocked_pywc = MagicMock()

        main(options, mocked_pywc)

        printed_message = stdout.getvalue().strip()

        self.assertIn('Option not valid', printed_message)

        os.remove(filename)

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_no_option(self, stdout):
        filename = 'test_no_option.txt'
        file_string = '''word1 word2
        word3
        word4
        '''
        bytes_length = 25
        lines_length = 3
        words_length = 4

        with open(filename, 'w') as file:
            file.write(file_string)

        options = ['pywc.py', filename]

        mocked_pywc = MagicMock()
        mocked_pywc.count.return_value = [bytes_length, lines_length, words_length]
        main(options, mocked_pywc)

        printed_message = stdout.getvalue().strip()

        self.assertEqual(f'{bytes_length} bytes - {lines_length} lines - {words_length} words {filename}',
                         printed_message)

        os.remove(filename)

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_no_option_1(self, stdout):
        filename = 'test_no_option.txt'
        file_string = 'w'
        bytes_length = 1
        lines_length = 1
        words_length = 1

        with open(filename, 'w') as file:
            file.write(file_string)

        options = ['pywc.py', filename]

        mocked_pywc = MagicMock()
        mocked_pywc.count.return_value = [bytes_length, lines_length, words_length]
        main(options, mocked_pywc)

        printed_message = stdout.getvalue().strip()

        self.assertEqual(f'{bytes_length} byte - {lines_length} line - {words_length} word {filename}',
                         printed_message)

        os.remove(filename)

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_no_file(self, stdout):

        stream_length = 1000

        options = ['pywc.py', '-c']

        mocked_pywc = MagicMock()
        mocked_pywc.count.return_value = [stream_length]

        main(options, mocked_pywc)

        stream_string = 'x' * stream_length
        sys.stdin = io.StringIO(stream_string)

        printed_message = stdout.getvalue().strip()

        self.assertEqual(f"{stream_length} bytes", printed_message.strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_error_wrong_file(self, stdout):
        filename = 'test_c_option_10.txt'
        file_length = 100

        with open(filename, 'w') as file:
            file.write('x' * file_length)

        options = ['pywc.py', '-c', 'xxx']

        mocked_pywc = MagicMock()

        main(options, mocked_pywc)

        printed_message = stdout.getvalue().strip()

        self.assertEqual("File 'xxx' does not exist.", printed_message)

        os.remove(filename)
