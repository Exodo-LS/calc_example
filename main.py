"""Content of calculator.py#"""


def inc(x_value):
    """Increment function adds 1 to the x_value"""
    return x_value + 1


def test_answer():
    """This function validates that the Increment Function"""
    assert inc(4) == 5
