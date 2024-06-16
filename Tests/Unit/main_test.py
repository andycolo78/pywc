import os
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

        mocked_pywc.set_file.assert_called_with(filename)
        mocked_pywc.count_bytes.assert_called()
        mocked_pywc.count_bytes.return_value = file_length

        os.remove(filename)

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_c_option(self, stdout):

        filename = 'test_c_option_1M.txt'
        file_length = 1000000

        with open(filename, 'w') as file:
            file.write('x' * file_length)

        options = ['pywc.py', '-c', filename]

        mocked_pywc = MagicMock()
        mocked_pywc.count_bytes.return_value = file_length

        main(options, mocked_pywc)

        printed_message = stdout.getvalue().strip()

        self.assertEqual(f"{file_length} bytes {filename}", printed_message)

        os.remove(filename)

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_l_option(self, stdout):

        filename = 'test_l_option_1000.txt'
        lines_number = 1000

        with open(filename, 'w') as file:
            file.write('zxcvbnmasdfghjklqwertyuiop1234567890\n' * lines_number)

        options = ['pywc.py', '-l', filename]

        mocked_pywc = MagicMock()
        mocked_pywc.count_lines.return_value = lines_number

        main(options, mocked_pywc)

        printed_message = stdout.getvalue().strip()

        self.assertEqual(f"{lines_number} lines {filename}", printed_message)

        os.remove(filename)

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_wrong_option(self, stdout):
        filename = 'test_c_option_10.txt'
        file_length = 100

        with open(filename, 'w') as file:
            file.write('x' * file_length)

        options = ['pywc.py', '-x', filename]

        mocked_pywc = MagicMock()
        mocked_pywc.count_bytes.return_value = file_length

        main(options, mocked_pywc)

        printed_message = stdout.getvalue().strip()

        self.assertIn('Option not valid', printed_message)

        os.remove(filename)

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_no_option(self, stdout):
        filename = 'test_c_option_10.txt'
        file_length = 100

        with open(filename, 'w') as file:
            file.write('x' * file_length)

        options = ['pywc.py', filename]

        mocked_pywc = MagicMock()

        main(options, mocked_pywc)

        printed_message = stdout.getvalue().strip()

        self.assertEqual("Usage: python pywc.py -option <filename>", printed_message)

        os.remove(filename)

    @patch('sys.stdout', new_callable=StringIO)
    def test_main_no_file(self, stdout):

        options = ['pywc.py', '-c']

        mocked_pywc = MagicMock()

        main(options, mocked_pywc)

        printed_message = stdout.getvalue().strip()

        self.assertEqual("Usage: python pywc.py -option <filename>", printed_message)


    @patch('sys.stdout', new_callable=StringIO)
    def test_main_error_wrong_file(self, stdout):
        filename = 'test_c_option_10.txt'
        file_length = 100

        with open(filename, 'w') as file:
            file.write('x' * file_length)

        options = ['pywc.py', '-c', 'xxx']

        mocked_pywc = MagicMock()
        mocked_pywc.count_bytes.return_value = file_length

        main(options, mocked_pywc)

        printed_message = stdout.getvalue().strip()

        self.assertEqual("File 'xxx' does not exist.", printed_message)

        os.remove(filename)
