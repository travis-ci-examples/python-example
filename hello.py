from __future__ import print_function
import sys


def hello(what):
    print('Hello, {}!'.format(what))


def say_what():
    return 'world'


def main():
    hello(say_what())
    return 0


if __name__ == '__main__':
    sys.exit(main())
