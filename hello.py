from __future__ import print_function
import sys


def hello(what):
    print('Hello, {}!'.format(what))


def say_what():
    return 'wor'


def main():
    hello(say_what())
    print('lol1')
    print('xd')
    return 0


if __name__ == '__main__':
    sys.exit(main())
