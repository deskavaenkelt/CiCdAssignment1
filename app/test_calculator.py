from calculator import addition, subtraction


def test_addition1():
    assert addition(2, 2) == 4


def test_addition2():
    assert addition(2, 2) != 3


def test_subtraction1():
    assert subtraction(6, 2) == 4


def test_subtraction2():
    assert addition(2, 2) != 3
