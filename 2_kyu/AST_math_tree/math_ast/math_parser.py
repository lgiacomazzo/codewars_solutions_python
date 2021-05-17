from typing import Iterable

from math_ast.arith_op import ArithOp
from math_ast.math_expressions import MathExpressionInterface, LiteralValue, BinaryOperator


class BidirectionalIterator:
    """
    Utility class used to implement a bidirectional iterator (currently only forward is used)
    """
    def __init__(self, expression: Iterable):
        self.expression = expression
        self.index = 0
        self.current_elem = self.expression[self.index]

    def move_forward(self):
        """
        Used to point the iterator to the next element
        """
        if self.index < len(self.expression) - 1:
            self.index += 1
            self.current_elem = self.expression[self.index]
        else:
            self.current_elem = None

    def move_backward(self):
        """
        Used to point the iterator to the previous element
        """
        # Not used
        if self.index > 0:
            self.index -= 1
            self.current_elem = self.expression[self.index]
        else:
            self.current_elem = None

    def get_value(self):
        """
        Returns the current element pointed by the iterator
        :return: Current element pointed
        """
        return self.current_elem


class ParserException(Exception):
    """
    Represents an exception raised by the parse method of the parser
    """


class MathParser:
    """
    Simplified version of a parser, only for math expressions (no variables)
    note: ((...)) means optional, [...] means alternative (and | is to separate options)
    definitions used:
        expression := [+|-] term (( [+|-] term (( [+|-] term ((...))))))
        term := factor (( [*|/] factor (( [*|/] factor ((...))))))
        factor := [number | (expression) | -(expression) | +(expression)]
    """
    operators = ("+", "-", "*", "/", "(", ")")

    def __init__(self, expression: str):
        self.iterator = BidirectionalIterator("".join(expression.split()))

    def get_number(self):
        """
        It gets a number starting from the character pointed by the iterator, and updates the
        iterator skipping all characters read
        :return: A string that represents an integer or a float
        """
        number = None
        while self.iterator.get_value() is not None and \
                (self.iterator.get_value().isdigit() or self.iterator.get_value() == "."):
            number = self.iterator.get_value() if number is None \
                else number + self.iterator.get_value()
            self.iterator.move_forward()
        return number

    def get_operator(self):
        """
        It gets an operator starting from the character pointed by the iterator
        and updates the iterator skipping all characters read
        :return: A string representing an operator (as contained in MathParser.operators)
        """
        operator = None
        if self.iterator.get_value() in MathParser.operators:
            operator = self.iterator.get_value()
            self.iterator.move_forward()
        return operator

    def parse_factor(self) -> MathExpressionInterface:
        """
        Composes an AST tree for a factor according to this definition:
        factor := [ number | (expression) | -(expression) | +(expression) ]
        """
        root_ast = None
        number = self.get_number()
        if number is not None:
            root_ast = LiteralValue(number)
        else:
            operator = self.get_operator()
            if operator == '-':
                # for me, the negate [- term] will be the same as [0 - term]
                root_ast = BinaryOperator(operator=ArithOp.map[operator],
                                          left_expression=LiteralValue(0),
                                          right_expression=self.parse_factor())
            elif operator == "+":
                root_ast = self.parse_factor()
            elif operator == "(":
                root_ast = self.parse_expression()
                operator = self.get_operator()
                if operator != ")":
                    print("Error in the parse_factor method, operator = " + str(operator))
        return root_ast

    def parse_term(self) -> MathExpressionInterface:
        """
        Composes an AST tree for a term according to this definition:
        term := factor (([* |/] factor (([* | /] factor ((...))))))
        """
        root_ast, interesting_ops = self.parse_factor(), ("*", "/")

        while self.iterator.get_value() in interesting_ops:
            operator = self.get_operator()
            temp_root_ast = self.parse_factor()
            root_ast = BinaryOperator(operator=ArithOp.map[operator],
                                      left_expression=root_ast,
                                      right_expression=temp_root_ast)

        return root_ast

    def parse_expression(self) -> MathExpressionInterface:
        """
        Composes an AST tree for an expression according to this definition:
        expression := [+|-] term (( [+|-] term (( [+|-] term ((...))))))
        """

        root_ast, leading_sign, interesting_ops = None, None, ("+", "-")
        if self.iterator.get_value() in interesting_ops:
            leading_sign = self.get_operator()

        root_ast = self.parse_term()

        if leading_sign == "-":
            # for me, the negate [- term] will be the same as [0 - term]
            root_ast = BinaryOperator(operator=ArithOp.map[leading_sign],
                                      left_expression=LiteralValue(0),
                                      right_expression=root_ast)

        while self.iterator.get_value() in interesting_ops:
            operator = self.get_operator()
            temp_root_ast = self.parse_term()
            root_ast = BinaryOperator(operator=ArithOp.map[operator],
                                      left_expression=root_ast,
                                      right_expression=temp_root_ast)
        return root_ast

    def parse(self):
        """
        Public function to be called for parsing a math expression
        :return: The AST tree as result of the expression parsing
        """
        try:
            return self.parse_expression()
        except Exception as exception:
            raise ParserException("Something bad happened. Please check your formula") \
                from exception
