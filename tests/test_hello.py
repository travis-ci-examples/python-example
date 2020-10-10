import hello


def test_says_world():
    assert hello.say_what() == 'world'

def test_says_world2():
    assert hello.say_what() == 'world2'
