import unittest

from pywc import parse_argv


class ParseArgvTest(unittest.TestCase):

    def test_option_and_filename(self):

        argv = ['pywc.py', '-c', 'test_file.txt']

        expected_result = {'option': '-c', 'filename': 'test_file.txt'}
        result = parse_argv(argv)

        self.assertDictEqual(expected_result, result)

    def test_filename_only(self):
        argv = ['pywc.py', 'test_file.txt']

        expected_result = {'option': None, 'filename': 'test_file.txt'}
        result = parse_argv(argv)

        self.assertDictEqual(expected_result, result)

    def test_option_only(self):
        argv = ['pywc.py', '-c']

        expected_result = {'option': '-c', 'filename': None}
        result = parse_argv(argv)

        self.assertDictEqual(expected_result, result)

    def test_no_args(self):
        argv = ['pywc.py']

        expected_result = {'option': None, 'filename': None}
        result = parse_argv(argv)

        self.assertDictEqual(expected_result, result)
