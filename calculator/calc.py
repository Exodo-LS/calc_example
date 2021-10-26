"""Content of calculator.py#"""


def inc(x_value):
    """Increment function adds 1 to the x_value"""
    return x_value + 1


class Calculator:
    """This will be the defined Calculator class"""
    output = 0

    def get_output(self):
        """Returns the current value of the Calculator"""
        return self.output

    def addition(self, input_value1, input_value2):
        """This function performs addition"""
        self.output = input_value1 + input_value2
        return self.output

    def subtraction(self, input_value1, input_value2):
        """This function performs subtraction"""
        self.output = input_value1 - input_value2
        return self.output

    def multiplication(self, input_value1, input_value2):
        """This function performs multiplication"""
        self.output = input_value1 * input_value2
        return self.output

    def division(self, input_value1, input_value2):
        """This function does division"""
        try:
            self.output = input_value1 / input_value2
        except ZeroDivisionError:
            self.output = 0
        return self.output
