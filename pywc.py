import os
import sys
from Utils.pywc import Pywc

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
'''
option_not_valid_lbl = '''
Option not valid. Allowed options: -c, -l    
'''


def main(argv: list, pywc: Pywc) -> None:

    if len(argv) < 3:
        print(usage_lbl)
        return

    filename = argv[2]

    if not os.path.isfile(filename):
        print(f"File '{filename}' does not exist.")
        return

    pywc.set_file(filename)

    if '-c' in argv:
        result = pywc.count_bytes()
        print(f"{result} bytes {filename}")
        return

    if '-l' in argv:
        result = pywc.count_lines()
        print(f"{result} lines {filename}")
        return

    print(option_not_valid_lbl)


if __name__ == "__main__":
    main(sys.argv, Pywc())
