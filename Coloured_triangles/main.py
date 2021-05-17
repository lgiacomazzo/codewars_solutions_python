from tests.tests import tests
import Fast_solution.count as fast_count
import Slow_solution.count as slow_count


# https://www.codewars.com/kata/57cebf1472f98327760003cd


def test():

    func_list = [
        fast_count.count_col_triangle,
        slow_count.count_col_triangle
    ]

    for input_, result in tests:
        for func in func_list:
            returned_result = func(input_)
            if returned_result != result:
                raise Exception("Different result, this was required: " +
                                str(result) +
                                ", and this was obtained: " +
                                str(returned_result)
                                )
    print("Tests passed")


if __name__ == "__main__":
    test()
