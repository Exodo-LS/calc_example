"""Content of calc.py"""
from calculator.operations.addition import Addition
from calculator.operations.subtraction import Subtraction
from calculator.operations.multiplication import Multiplication
from calculator.operations.division import Division

class Calculator:
    """This will be the defined Calculator class"""

    @staticmethod
    def addition(value_a, value_b):
        """This function performs addition"""
        return Addition.add(value_a,value_b)

    @staticmethod
    def subtraction(value_a, value_b):
        """This function performs subtraction"""
        return Subtraction.subtract(value_a,value_b)

    @staticmethod
    def multiplication(value_a, value_b):
        """This function performs multiplication"""
        return Multiplication.multiply(value_a, value_b)

    @staticmethod
    def division(value_a, value_b):
        """This function does division"""
        try:
            output = Division.divide(value_a,value_b)
        except ZeroDivisionError:
            output = 0
        return output
