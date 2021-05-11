from math_ast.math_parser import MathParser, ParserException
from expressions_test import tests
# https://www.codewars.com/kata/52a78825cdfc2cfc87000005


def calc(expression):
    """
    Primary method used for starting parsing and evaluation of a single expression
    :param expression:
    :return:
    """
    parser = MathParser(expression)
    elem = parser.parse()
    return elem.evaluate()

def test():
    """
    Test method, check whether all the expression tests are successful
    """
    index = 0
    for expression, result in tests:
        index += 1
        try:
            print("------------ Next -------------")
            result_obtained = calc(expression)
            if result_obtained == result:
                print(result_obtained, "->", result)
            else:
                print(str(index) +
                      " - Ottenuto " +
                      str(result_obtained) +
                      ", ma dovevo ottenere " +
                      str(result)
                )
        except ParserException as exception:
            print(str(index) + ": " + print(exception))

def start_mfi():
    """
    Method used for starting the interpreter interface
    :return:
    """
    print("Starting math formulas interpreter 0.1. Press 'q' to stop.")
    while True:
        expression = input("formula> ")
        if expression == "":
            continue
        if expression == "q":
            break
        try:
            print(calc(expression))
        except ParserException as exception:
            print(exception)

if __name__ == '__main__':
    start_mfi()
