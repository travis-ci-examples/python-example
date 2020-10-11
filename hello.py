from __future__ import print_function
import sys


def hello(what):
    print('Hello, {}!'.format(what))


def say_what():
    return 'world'

def add_numbers(a, b):
    result = a+b
    return result

def main():
    hello(say_what())
    add_numbers(2, 2)
    add_numbers(3, 3)
    add_numbers(4, 4)
    add_numbers(5, 5)
    print('lol1')
    print('xd')
    return 0


if __name__ == '__main__':
    sys.exit(main())
