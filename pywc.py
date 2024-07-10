import os
import sys

import select

from App.Readers.file_reader import FileReader
from App.Readers.stdin_reader import StdinReader
from App.pywc import Pywc
from App.Counters.bytes_counter import BytesCounter
from App.Counters.lines_counter import LinesCounter
from App.Counters.words_counter import WordsCounter

'''
Available options:
* -c : count bytes
* -l : count lines
'''

usage_lbl = '''
Usage: python pywc.py option <filename>
options:
-c : count bytes
-l : count lines
-w : count words
no option : count bytes, lines and words
'''

option_not_valid_lbl = '''
Option not valid. Allowed options: -c, -l, -w or no option
'''

valid_options = ['-c', '-l', '-w']


def main(argv: list, pywc: Pywc) -> None:
    params = parse_argv(argv)

    if params['filename'] is None:
        if sys.stdin.isatty() and not select.select([sys.stdin], [], [], 0.0)[0]:
            print(usage_lbl)
            return
        reader = StdinReader()
    else:
        if not os.path.isfile(params['filename']):
            print(f"File '{params['filename']}' does not exist.")
            return
        reader = FileReader(params['filename'])

    pywc.set_reader(reader)

    if params['option'] is None:
        result = pywc.count([BytesCounter(), LinesCounter(), WordsCounter()])
        print(
            f"{result[0]} {'byte' if result[0] == 1 else 'bytes'} "
            f"- {result[1]} {'line' if result[1] == 1 else 'lines'} "
            f"- {result[2]} {'word' if result[2] == 1 else 'words'} "
            f"{'' if params['filename'] is None else params['filename']}")
        return

    if '-c' in params['option']:
        result = pywc.count([BytesCounter()])
        print(f"{result[0]} {'byte' if result[0] == 1 else 'bytes'} " 
              f"{'' if params['filename'] is None else params['filename']}")
        return

    if '-l' in params['option']:
        result = pywc.count([LinesCounter()])
        print(f"{result[0]} {'line' if result[0] == 1 else 'lines'} "
              f"{'' if params['filename'] is None else params['filename']}")
        return

    if '-w' in params['option']:
        result = pywc.count([WordsCounter()])
        print(f"{result[0]} {'word' if result[0] == 1 else 'words'} "
              f"{'' if params['filename'] is None else params['filename']}")
        return

    print(option_not_valid_lbl)


def parse_argv(argv: list) -> dict:
    result = {'option': None, 'filename': None}

    if len(argv) < 2:
        return result

    for arg in argv[1:]:
        if len(arg) == 2 and arg.startswith('-'):
            result['option'] = arg
            continue
        result['filename'] = arg

    return result


if __name__ == "__main__":
    main(sys.argv, Pywc())
