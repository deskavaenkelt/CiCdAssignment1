from calculator import addition, subtraction, multiplication, division


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


def test_division1():
    assert division(6, 2) == 3


def test_division2():
    assert division(2, 2) != 3


def test_division3():
    assert division(2, 0) == 0
