from tests.tests import tests
from classless.iterative import escape as classless_iterative_escape
from classless.recursive import escape as classless_recursive_escape
from classful.iterative_maze_solver import IterativeMazeSolver
from classful.recursive_maze_solver import RecursiveMazeSolver

# https://www.codewars.com/kata/5877027d885d4f6144000404

# Return the array of movements to execute to get out of the maze

func_list = [
    classless_iterative_escape,
    classless_recursive_escape
]


def test_classless():
    print("------------Classless--------------")
    for func in func_list:
        print("Proving " + func.__name__)
        for maze, result in tests:
            func_result = func(maze)
            if func_result != result:
                raise Exception("Path generated is different: " + str(func_result))
            print("-----------------------------------")
        print("Tests passed")


class_list = [
    IterativeMazeSolver,
    RecursiveMazeSolver
]


def test_classful():
    print("------------Classful--------------")
    for cls in class_list:
        print("Proving " + cls.__name__)
        for maze, result in tests:
            solver = cls(maze)
            func_result = solver.escape()
            if func_result != result:
                raise Exception("Path generated is different: " + str(func_result))
            print("-----------------------------------")
        print("Tests passed")


def test():
    test_classful()
    test_classless()


if __name__ == "__main__":
    test()
