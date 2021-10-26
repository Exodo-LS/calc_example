"""This class will hold all the operations"""

class Operator:
    """This class will hold the static addition, subtraction, multiplication and division methods"""

    @staticmethod
    def add(value_a, value_b):
        """This method adds value_a and value_b"""
        return value_a + value_b

    @staticmethod
    def subtract(value_a, value_b):
        """This method subtracts value_a and value_b"""
        return value_a - value_b

    @staticmethod
    def multiply(value_a, value_b):
        """This method multiplies value_a and value_b"""
        return value_a * value_b

    @staticmethod
    def divide(value_a, value_b):
        """This method divides value_a and value_b"""
        return (value_a / value_b) if value_b != 0 else 0
