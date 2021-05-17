class ArithOp:
    """
    Utility class that stores mathematical operations to be applied
    """
    @staticmethod
    def plus(left_expression, right_expression):
        """
        Plus operator
        :param left_expression: Instance of MathExpressionInterface
        :param right_expression: Instance of MathExpressionInterface
        :return: Value (not objects) of the operation
        """
        return left_expression.evaluate() + right_expression.evaluate()

    @staticmethod
    def minus(left_expression, right_expression):
        """
        Minus operator
        :param left_expression: Instance of MathExpressionInterface
        :param right_expression: Instance of MathExpressionInterface
        :return: Value (not objects) of the operation
        """
        return left_expression.evaluate() - right_expression.evaluate()

    @staticmethod
    def mul(left_expression, right_expression):
        """
        Multiply operator
        :param left_expression: Instance of MathExpressionInterface
        :param right_expression: Instance of MathExpressionInterface
        :return: Value (not objects) of the operation
        """
        return left_expression.evaluate() * right_expression.evaluate()

    @staticmethod
    def div(left_expression, right_expression):
        """
        Divide operator
        :param left_expression: Instance of MathExpressionInterface
        :param right_expression: Instance of MathExpressionInterface
        :return: Value (not objects) of the operation
        """
        return left_expression.evaluate() / right_expression.evaluate()

    map = {
        "+": plus.__func__,
        "-": minus.__func__,
        "*": mul.__func__,
        "/": div.__func__
    }
