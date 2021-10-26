"""Testing to see if the Calculator works"""
from calculator.main import Calculator


def test_calculator_output():
    """Verifying that output is 3"""
    calc = Calculator()
    assert calc.output == 3

def test_calculator_addition():
    """Testing the addition function"""
    calc = Calculator()
    calc.addition(3)
    assert calc.output == 6

def test_calculator_subtraction():
    """Testing the subtraction function"""
    calc = Calculator()
    calc.subtraction(1)
    assert calc.output == 2

def test_calculator_multiplication():
    """Testing the multiplication function"""
    calc = Calculator()
    calc.multiplication(4)
    assert calc.output == 12

def test_calculator_division():
    """Testing the division function"""
    calc = Calculator()
    calc.division(calc.output)
    assert calc.output == 1
