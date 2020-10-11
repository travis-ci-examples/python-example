from hello import *


def test_says_world():
    assert hello.say_what() == 'world'

def test_1():
    assert add_numbers(2, 2) == 4
def test_2():
    assert add_numbers(3, 3) == 6
def test_3():
    assert add_numbers(4, 4) == 8
def test_4():
    assert add_numbers(5, 5) == 10
