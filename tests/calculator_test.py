"""Testing to see if the Calculator works"""
from calculator.main import Calculator


def test_calculator_answer():
    """Verifying that answer is 2"""
    calc = Calculator()
    assert calc.answer == 2


def test_calculator_addition():
    """Testing the addition function"""
    calc = Calculator()
    calc.addition(1)
    assert calc.answer == 3


def test_calculator_subtraction():
    """Testing the subtraction function"""
    calc = Calculator()
    calc.subtraction(1)
    assert calc.answer == 1


def test_calculator_multiplication():
    """Testing the multiplication function"""
    calc = Calculator()
    calc.multiplication(3)
    assert calc.answer == 6


def test_calculator_division():
    """Testing the division function"""
    calc = Calculator()
    calc.division(2)
    assert calc.answer == 1
