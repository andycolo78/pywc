import os
import sys

from App.Readers.file_reader import FileReader
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
    if len(argv) < 2:
        print(usage_lbl)
        return

    if len(argv) < 3 and argv[1] in valid_options:
        print(usage_lbl)
        return

    option = None if len(argv) < 3 else argv[1]
    filename = argv[1] if len(argv) == 2 else argv[2]

    if not os.path.isfile(filename):
        print(f"File '{filename}' does not exist.")
        return

    file_reader = FileReader(filename)
    pywc.set_reader(file_reader)

    if option is None:
        result = pywc.count([BytesCounter(), LinesCounter(), WordsCounter()])
        print(
            f"{result[0]} {'byte' if result[0] == 1 else 'bytes'} "
            f"- {result[1]} {'line' if result[1] == 1 else 'lines'} "
            f"- {result[2]} {'word' if result[2] == 1 else 'words'} {filename}")
        return

    if '-c' in option:
        result = pywc.count([BytesCounter()])
        print(f"{result[0]} {'byte' if result[0] == 1 else 'bytes'} {filename}")
        return

    if '-l' in option:
        result = pywc.count([LinesCounter()])
        print(f"{result[0]} {'line' if result[0] == 1 else 'lines'} {filename}")
        return

    if '-w' in option:
        result = pywc.count([WordsCounter()])
        print(f"{result[0]} {'word' if result[0] == 1 else 'words'} {filename}")
        return

    print(option_not_valid_lbl)


if __name__ == "__main__":
    main(sys.argv, Pywc())
