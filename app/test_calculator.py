from calculator import addition, subtraction, multiplication


def test_addition1():
    assert addition(2, 2) == 4


def test_addition2():
    assert addition(2, 2) != 3


def test_subtraction1():
    assert subtraction(6, 2) == 4


def test_subtraction2():
    assert addition(2, 2) != 3


def test_multiplication1():
    assert multiplication(6, 2) == 12


def test_multiplication2():
    assert multiplication(2, 2) != 3
