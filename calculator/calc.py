"""Content of calc.py"""
from calculator.operations.operator import Operator

class Calculator:
    """This will be the defined Calculator class"""

    @staticmethod
    def addition(value_a, value_b):
        """This function performs addition"""
        return Operator.add(value_a,value_b)

    @staticmethod
    def subtraction(value_a, value_b):
        """This function performs subtraction"""
        return Operator.subtract(value_a,value_b)

    @staticmethod
    def multiplication(value_a, value_b):
        """This function performs multiplication"""
        return Operator.multiply(value_a, value_b)

    @staticmethod
    def division(value_a, value_b):
        """This function performs division"""
        return Operator.divide(value_a, value_b)
