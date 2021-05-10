# Composite pattern
from typing import Callable


class MathExpressionInterface:
    """
    Acts as a sort of interface
    """

    def evaluate(self):
        """
        Method to be defined in a subclass. It returns a value (not an object)
        according to an operator or not
        :return: integer or float
        """

    def __str__(self):
        """
        Method to be defined in a subclass. It's a representation of the value computed
        according to the expression stored
        :return: integer or float
        """


class LiteralValue(MathExpressionInterface):
    """
    It represents a value (an integer or a float), which is an expression
    evaluated to itself (for example 50, or 10.9)
    """
    def __init__(self, value):
        if isinstance(value, str):
            try:
                value = int(value)
            except ValueError:
                value = float(value)
        self.value = value
        # self.value = Decimal(value)

    def evaluate(self):
        return self.value

    def __str__(self):
        return str(self.value)


class BinaryOperator(MathExpressionInterface):
    """
    It represents an expression composed of a binary operator (+, -, *, /) and
    a left and a right MathExpressionInterface subclass. It's evaluated to the result of
    the previously explained expression.
    """
    def __init__(
            self,
            operator: Callable,
            left_expression: MathExpressionInterface,
            right_expression: MathExpressionInterface
    ):
        self.operator = operator
        self.left_expression = left_expression
        self.right_expression = right_expression

    def evaluate(self):
        return LiteralValue(self.operator(self.left_expression, self.right_expression)).evaluate()

    def __str__(self):
        return str(LiteralValue(self.operator(self.left_expression, self.right_expression)))
