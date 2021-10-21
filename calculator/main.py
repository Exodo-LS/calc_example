"""Content of calculator.py#"""


def inc(x_value):
    """Increment function adds 1 to the x_value"""
    return x_value + 1


class Calculator:
    """This will be the defined Calculator class"""
    answer = 2

    def get_answer(self):
        """Returns the current value of the Calculator"""
        return self.answer

    def addition(self, u_value):
        """This function performs addition"""
        self.answer = self.answer + u_value
        return self.answer

    def subtraction(self, u_value):
        """This function performs subtraction"""
        self.answer = self.answer - u_value
        return self.answer

    def multiplication(self, u_value):
        """This function performs multiplication"""
        self.answer = self.answer * u_value
        return self.answer

    def division(self, u_value):
        """This function performs division"""
        try:
            self.answer = self.answer / u_value
        except ZeroDivisionError:
            self.answer = 0
        return self.answer
