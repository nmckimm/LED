#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Program entry point"""

from __future__ import print_function

import argparse
import sys
from lights import LightTester
from led_module import metadata


def main(argv):
    """Program entry point.

    :param argv: command-line arguments
    :type argv: :class:`list`
    """

    lights = LightTester.lights


    parser = argparse.ArgumentParser()
    parser.add_argument('input.txt')
    args = parser.parse_args()
    with open(args.filename) as file:
    # do stuff here
        for cmd in file:
            lights.apply(cmd)
        print("#occupied: ", lights.count())

    author_strings = []
    for name, email in zip(metadata.authors, metadata.emails):
        author_strings.append('Author: {0} <{1}>'.format(name, email))

    epilog = '''
{project} {version}

{authors}
URL: <{url}>
'''.format(
        project=metadata.project,
        version=metadata.version,
        authors='\n'.join(author_strings),
        url=metadata.url)

    arg_parser = argparse.ArgumentParser(
        prog=argv[0],
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=metadata.description,
        epilog=epilog)
    arg_parser.add_argument(
        '-V', '--version',
        action='version',
        version='{0} {1}'.format(metadata.project, metadata.version))

    arg_parser.parse_args(args=argv[1:])

    print(epilog)



    return 0

'''def main(file, N):
    lights = LightTester(N)
    file = open(input.txt, 'r')
    lines = file.readlines()
    file.close()

    for cmd in file:
        lights.apply(cmd)
    print("#occupied: ", lights.count())
'''


def entry_point():
    """Zero-argument entry point for use with setuptools/distribute."""
    raise SystemExit(main(sys.argv))


if __name__ == '__main__':
    entry_point()