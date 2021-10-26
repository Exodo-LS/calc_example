"""Testing to see if the Calculator works"""
from calculator.calc import Calculator

def test_calc_add():
    """This tests the Addition Function"""
    assert Calculator.addition(1,2) == 3

def test_calc_subtract():
    """This tests the Subtraction Function"""
    assert Calculator.subtraction(4,8) == -4

def test_calc_multiply():
    """This tests the Multiplication Function"""
    assert Calculator.multiplication(25, 4) == 100

def test_calc_divide():
    """This tests the Division Function"""
    assert Calculator.division(6,6) == 1
