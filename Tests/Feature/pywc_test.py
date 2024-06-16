import subprocess
import unittest
from parameterized import parameterized


class PywcTest(unittest.TestCase):

    @parameterized.expand([
        ("test_c_10", '-c', '.\\Tests\\Dataset\\test_c_option_10.txt',
         '10 bytes .\\Tests\\Dataset\\test_c_option_10.txt'),
        ("test_c_100", '-c', '.\\Tests\\Dataset\\test_c_option_100.txt',
         '100 bytes .\\Tests\\Dataset\\test_c_option_100.txt'),
        ("test_c_1M", '-c', '.\\Tests\\Dataset\\test_c_option_1M.txt',
         '1000000 bytes .\\Tests\\Dataset\\test_c_option_1M.txt'),
        ("test_l_10", '-l', '.\\Tests\\Dataset\\test_l_option_10.txt',
         '10 lines .\\Tests\\Dataset\\test_l_option_10.txt'),
        ("test_l_10_no_termination", '-l', '.\\Tests\\Dataset\\test_l_option_10_no_termination.txt',
         '10 lines .\\Tests\\Dataset\\test_l_option_10_no_termination.txt'),
        ("test_no_option", '', '.\\Tests\\Dataset\\test_c_option_1M.txt',
         'Usage: python pywc.py -option <filename>'),
        ("test_wrong_option", '-x', '.\\Tests\\Dataset\\test_c_option_1M.txt',
         'Option not valid. Allowed options: -c'),
        ("test_no_file", '-c', '',
         'Usage: python pywc.py -option <filename>'),
        ("test_wrong_file", '-c', '.\\xxx.txt',
         'File \'.\\xxx.txt\' does not exist.')
    ])
    def test_pywc(self, name, command, test_file, expected):
        args = ['python', 'pywc.py']
        if len(command) > 0:
            args.append(command)
        if len(test_file) > 0:
            args.append(test_file)

        result = subprocess.run(args, capture_output=True, text=True, cwd='.\\..\\..\\')

        self.assertEqual(expected, result.stdout.strip())
