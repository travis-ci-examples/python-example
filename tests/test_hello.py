import hello


def test_says_world():
    assert hello.say_what() == 'world'

def test_says_mama():
    assert hello.say_mama() == 'mama'
