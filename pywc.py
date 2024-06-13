import os
import sys
from Utils.pywc import Pywc

'''
Available options:
* -c : count bytes
'''


def main(argv: list, pywc: Pywc) -> None:

    if len(argv) < 3:
        print("Usage: python pywc.py -option <filename>")
        return

    filename = argv[2]

    if not os.path.isfile(filename):
        print(f"File '{filename}' does not exist.")
        return

    pywc.set_file(filename)

    if '-c' in argv:
        result = pywc.count_bytes()
        print(f"{result} {filename}")
        return

    print(f"Option not valid. Allowed options: -c")


if __name__ == "__main__":
    main(sys.argv, Pywc())
