import main


def test_addition1():
    assert main.addition(2, 2) == 4


def test_addition2():
    assert main.addition(2, 2) != 3
