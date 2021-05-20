import math

from tests.tests import tests


# https://www.codewars.com/kata/5877e7d568909e5ff90017e6

def recursive_find_all(sum_dig, digs, first_digit, indent=0):
    list_numbers = []
    if digs == 0:
        if sum_dig == 0:
            list_numbers.append(first_digit)
            print("\t" * indent, "->", first_digit, ": sum_dig=", sum_dig, ",digs=", digs, ", OK")
        else:
            print("\t" * indent, "->", first_digit, ": sum_dig=", sum_dig, ",digs=", digs, ", NO OK")
        return list_numbers
    print("\t" * indent, "->", first_digit, ": sum_dig=", sum_dig, ",digs=", digs)
    for current_digit in range(first_digit, min(9, sum_dig) + 1):
        recursive_numbers = recursive_find_all(
            sum_dig - current_digit,
            digs - 1,
            current_digit,
            indent + 1
        )
        for partial_number in recursive_numbers:
            list_numbers.append(int(str(first_digit) + str(partial_number)))
    print("\t"*indent, "->", list_numbers)
    return list_numbers


def find_all(sum_dig, digs):
    # your code here
    if sum_dig > digs * 9:
        return []
    if sum_dig == digs * 9:
        value = int(str(9) * digs)
        return [1, value, value]

    final_result = []
    for current_digit in range(1, min(9, sum_dig) + 1):
        array_values = recursive_find_all(sum_dig-current_digit, digs-1, current_digit)
        for value in array_values:
            final_result.append(value)
    print(final_result)
    if len(final_result) > 0:
        return [len(final_result), min(final_result), max(final_result)]
    return []


def test():
    """
    Test method
    """
    func = find_all
    for arg, result in tests:
        result_func = func(*arg)
        print("arg:", arg, ", result desired:", result, ", result obtained:", result_func)
        if result_func != result:
            raise Exception("Test not passed")
        print("---------------------------------")
    print("Tests passed")


if __name__ == '__main__':
    test()
