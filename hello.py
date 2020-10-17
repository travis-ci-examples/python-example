from __future__ import print_function
import sys


def hello(what):
    print('Hello, {}!'.format(what))


def say_what():
    return 'world'

def say_what2():
    return 'world2'


def main():
    print("Hello World")
    hello(say_what())
    print("Hello World2")
    hello(say_what2())
    return 0

if __name__ == '__main__':
    sys.exit(main())
