from calculator import addition


def test_addition1():
    assert addition(2, 2) == 4


def test_addition2():
    assert addition(2, 2) != 3
