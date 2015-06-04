from __future__ import print_function

import argparse
import io
import sys

def detect_coffee(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check')
    args = parser.parse_args(argv)

    coffeescript_files = []
    for filename in args.filenames:
        if filename.endswith(".coffee"):
            cofeescript_files.append(filename)

    if len(coffeescript_files) > 0:
        for cs_file in coffeescript_files:
            print('CoffeScript file found: {0}'.format(cs_file))
        return 1
    else:
        return 0


if __name__ == '__main__':
    sys.exit(detect_coffee())