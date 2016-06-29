#!/usr/bin/python
from __future__ import print_function

import argparse
import io
import sys

def generate_error(type, counter, line, filename):
    return {'type': type, 'line_num': counter, 'line': line, 'filename': filename}

def detect_rspec_focus(argv=None):
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
                if 'fscenario' in line.lower():
                    err = generate_error('fscenario', counter, line, filename)
                    errors.append(err)
                if 'fdescribe' in line.lower():
                    err = generate_error('fdescribe', counter, line, filename)
                    errors.append(err)
                if 'fcontext' in line.lower():
                    err = generate_error('fcontext', counter, line, filename)
                    errors.append(err)
                if 'fit ' in line.lower():
                    err = generate_error('fit', counter, line, filename)
                    errors.append(err)
                if 'focus:' in line.lower():
                    err = generate_error('focus:', counter, line, filename)
                    errors.append(err)
                if ':focus =>' in line.lower():
                    err = generate_error('focus hashbang', counter, line, filename)
                    errors.append(err)
    if len(errors) > 0:
        for error in errors:
            output = "Found {0} on line {1} of {2}: {3}"
            output = output.format(error['type'], error['line_num'],
                                   error['filename'], error['line'])
            print(output)
        return 1
    else:
        return 0


if __name__ == '__main__':
    sys.exit(detect_rspec_focus())
