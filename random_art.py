from random import random
import math

# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    expr1 = lambda x, y: (x + y)/2 * cos(y) * tan(5 ** 4) *cos(pi * sin(pi * cos))
    expr2 = lambda x, y: (x - y)/2 * random()
    expr3 = lambda x, y: x * y/4 * random()
    expr4 = lambda x, y: tan(6 * x) * cos(x)
    expr5 = lambda y, x: (sin(pi)) + tan(y**2)
    return random.choice([expr1, expr2, expr3, expr4, expr5])



def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)
