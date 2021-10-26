"""Testing to see if the Calculator works"""
from calculator.calc import Calculator


def test_calculator_output():
    """Verifying that output is 0"""
    calc = Calculator()
    assert calc.output == 0

def test_calculator_addition():
    """Testing the addition function"""
    calc = Calculator()
    calc.addition(1,1)
    assert calc.output == 2

def test_calculator_subtraction():
    """Testing the subtraction function"""
    calc = Calculator()
    calc.subtraction(0,1)
    assert calc.output == -1

def test_calculator_multiplication():
    """Testing the multiplication function"""
    calc = Calculator()
    calc.multiplication(4,25)
    assert calc.output == 100

def test_calculator_division():
    """Testing the division function"""
    calc = Calculator()
    calc.division(10,2)
    assert calc.output == 5
