import hello


def test_says_wor1ld():
    assert hello.say_what() == 'wor1ld'

def test_say_world():
    assert hello.say_what() == 'world'

def test_dummy1():
    assert 'world' == 'world'

def test_dummy2():
    assert '1' == '1'

def test_dummy3():
    assert '2' == '2'