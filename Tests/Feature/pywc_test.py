import subprocess
import unittest
from parameterized import parameterized


class PywcTest(unittest.TestCase):

    @parameterized.expand([
        ("test_c_1", '-c', '.\\Tests\\Dataset\\test_c_option_1.txt',
         '1 byte .\\Tests\\Dataset\\test_c_option_1.txt'),
        ("test_c_10", '-c', '.\\Tests\\Dataset\\test_c_option_10.txt',
         '10 bytes .\\Tests\\Dataset\\test_c_option_10.txt'),
        ("test_c_100", '-c', '.\\Tests\\Dataset\\test_c_option_100.txt',
         '100 bytes .\\Tests\\Dataset\\test_c_option_100.txt'),
        ("test_c_1M", '-c', '.\\Tests\\Dataset\\test_c_option_1M.txt',
         '1000000 bytes .\\Tests\\Dataset\\test_c_option_1M.txt'),
        ("test_l_1", '-l', '.\\Tests\\Dataset\\test_l_option_1.txt',
         '1 line .\\Tests\\Dataset\\test_l_option_1.txt'),
        ("test_l_10", '-l', '.\\Tests\\Dataset\\test_l_option_10.txt',
         '10 lines .\\Tests\\Dataset\\test_l_option_10.txt'),
        ("test_l_10_no_termination", '-l', '.\\Tests\\Dataset\\test_l_option_10_no_termination.txt',
         '10 lines .\\Tests\\Dataset\\test_l_option_10_no_termination.txt'),
        ("test_w_1", '-w', '.\\Tests\\Dataset\\test_w_option_1.txt',
         '1 word .\\Tests\\Dataset\\test_w_option_1.txt'),
        ("test_w_10", '-w', '.\\Tests\\Dataset\\test_w_option_10.txt',
         '10 words .\\Tests\\Dataset\\test_w_option_10.txt'),
        ("test_no_option", '', '.\\Tests\\Dataset\\test_no_option.txt',
         '78 bytes - 5 lines - 10 words .\\Tests\\Dataset\\test_no_option.txt'),
        ("test_wrong_option", '-x', '.\\Tests\\Dataset\\test_c_option_1M.txt',
         'Option not valid. Allowed options: -c, -l, -w or no option'),
        ("test_no_file", '-c', '',
         'Usage: python pywc.py option <filename>\noptions:\n-c : count bytes\n-l : count lines'
         '\n-w : count words\nno option : count bytes, lines and words'),
        ("test_wrong_file", '-c', '.\\xxx.txt',
         'File \'.\\xxx.txt\' does not exist.')
    ])
    def test_file_pywc(self, name, command, test_file, expected):
        args = ['python', 'pywc.py']
        if len(command) > 0:
            args.append(command)
        if len(test_file) > 0:
            args.append(test_file)

        result = subprocess.run(args, capture_output=True, text=True, cwd='.\\..\\..\\')

        self.assertEqual(expected, result.stdout.strip())

    @parameterized.expand([
        ("test_c_1", '-c', '.\\Tests\\Dataset\\test_c_option_1.txt',
         '1 byte'),
        ("test_c_10", '-c', '.\\Tests\\Dataset\\test_c_option_10.txt',
         '10 bytes'),
        ("test_c_100", '-c', '.\\Tests\\Dataset\\test_c_option_100.txt',
         '100 bytes'),
        ("test_c_1M", '-c', '.\\Tests\\Dataset\\test_c_option_1M.txt',
         '1000000'),
        ("test_l_1", '-l', '.\\Tests\\Dataset\\test_l_option_1.txt',
         '1 line'),
        ("test_l_10", '-l', '.\\Tests\\Dataset\\test_l_option_10.txt',
         '10 lines'),
        ("test_l_10_no_termination", '-l', '.\\Tests\\Dataset\\test_l_option_10_no_termination.txt',
         '10 lines'),
        ("test_w_1", '-w', '.\\Tests\\Dataset\\test_w_option_1.txt',
         '1 word'),
        ("test_w_10", '-w', '.\\Tests\\Dataset\\test_w_option_10.txt',
         '10 words'),
        ("test_no_option", '', '.\\Tests\\Dataset\\test_no_option.txt',
         '78 bytes - 5 lines - 10 words'),
        ("test_wrong_option", '-x', '.\\Tests\\Dataset\\test_c_option_1M.txt',
         'Option not valid. Allowed options: -c, -l, -w or no option')
    ])
    def test_stdin_pywc(self, name, command, test_file, expected):
        args = [f"cat {test_file}", 'python', 'pywc.py']
        if len(command) > 0:
            args.append(command)

        result = subprocess.run(args, capture_output=True, text=True, cwd='.\\..\\..\\')

        self.assertEqual(expected, result.stdout.strip())