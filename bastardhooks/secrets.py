#!/usr/bin/python
from __future__ import print_function

import argparse
import io
import re
import sys
from os.path import expanduser, isfile

def generate_error(type, counter, line, filename):
    return {'type': type, 'line_num': counter, 'line': line, 'filename': filename}

def secrets(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check')
    args = parser.parse_args(argv)

    scan_strings = []
    path = expanduser('~') + '/.secrets'
    if (isfile(path)):
        fh = open(path, "r")
        for line in fh.readlines():
            if len(line.strip()) > 0 and not line.startswith("#"):
                scan_strings.append(re.compile(line.strip()))
        fh.close()

    errors = []
    for filename in args.filenames:
        with io.open(filename, 'r') as f:
            content = f.readlines()
            counter = 0
            for line in content:
                counter = counter + 1
                for scanner in scan_strings:
                    if len(re.findall(scanner, line)) > 0:
                        err = generate_error(scanner.pattern, counter, line.strip(), filename)
                        errors.append(err)
    if len(errors) > 0:
        for error in errors:
            output = "Found {0} secret on line {1} of {2}: {3}"
            output = output.format(error['type'], error['line_num'],
                                   error['filename'], error['line'])
            print(output)
        return 1
    else:
        return 0


if __name__ == '__main__':
    sys.exit(secrets())
