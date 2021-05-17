from tests.tests import small_tests, medium_tests, big_tests
from Fast_solution.reduced_fractions import proper_fractions_fast
from Fast_solution.reduced_fractions import proper_fractions_fast_fast
from Slow_solution.reduced_fractions import proper_fractions_slow
from Slow_solution.reduced_fractions import proper_fractions_slow_slow
from Slow_solution.reduced_fractions import proper_fractions_slow_slow_slow
from Ultimate_solution.reduced_fractions import proper_fractions_ultimate_fast

# https://www.codewars.com/kata/55b7bb74a0256d4467000070

func_array = [
    proper_fractions_slow,
    proper_fractions_slow_slow,
    proper_fractions_slow_slow_slow,
    proper_fractions_fast,
    proper_fractions_fast_fast,
    proper_fractions_ultimate_fast
]


def test():
    """
    Test function, can select small tests (less than 100000), medium tests
    (less than 100000000), big tests (less than 10000000000)
    """
    choice_test = int(input("Small tests (0), medium tests (1), or big tests (2)? "))
    tests = small_tests if choice_test == 0 else medium_tests if choice_test == 1 else big_tests
    for function in func_array:
        print("Now starting tests for", function.__name__)
        print("---------------------------------")
        for arg, result in tests:
            result_func = function(arg)
            print("arg:", arg, ", result desired:", result, ", result obtained:", result_func)
            if result_func != result:
                raise Exception("Test not passed")
            print("---------------------------------")
        print("Tests passed")


def prod():
    """
    Gets input from user, and computes the number of reduced fractions with a
    given denominator
    """
    denominator = int(input("Insert the denominator desired: "))
    print("There are", proper_fractions_ultimate_fast(denominator), "reduced fractions with",
          denominator, "as the denominator")


if __name__ == '__main__':
    choice = int(input("Test mode (0) or prod mode (1)? "))
    func = test if choice == 0 else prod
    func()
