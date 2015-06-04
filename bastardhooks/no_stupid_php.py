#!/usr/bin/python
from __future__ import print_function

import argparse
import io
import sys

def generate_error(type, counter, line):
    return {'type': type, 'line_num': counter, 'line': line, 'filename': filename}

def detect_bad_php(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check')
    args = parser.parse_args(argv)

    errors = []
    for filename in args.filenames:
        with io.open(filename, 'r') as f:
            content = f.readlines()
            counter = 0
            for line in content:
                counter = counter + 1
                if 'magic_quotes' in line:
                    err = generate_error('magic_quotes', counter, line, filename)
                    errors.append(err)
                if 'extract($_get)' in line.lower():
                    err = generate_error('extract_get', counter, line, filename)
                    errors.append(err)
    if len(errors) > 0:
        for error in errors:
            output = "Found {0} error on line {1} of {2}: {3}"
            output = output.format(error['type'], error['line_num'],
                                   error['filename'], error['line']))
            print(output)
        return 1
    else:
        return 0


if __name__ == '__main__':
    sys.exit(detect_bad_php())
