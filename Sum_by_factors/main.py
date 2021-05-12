import old_solution.sum_factor as old_sum
import new_solution.sum_factor as new_sum
from tests.tests import tests

# https://www.codewars.com/kata/54d496788776e49e6b00052f

def main(function):
    for list_number, result in tests:
        if function(list_number) == result:
            print("ok for " + str(list_number))
        else:
            print("wrong for " + str(list_number))

if __name__ == "__main__":
    print("1) No classes")
    print("2) With classes")
    num = int(input("Select one: "))
    function = None
    if num == 1:
        function = old_sum.sum_for_list
    if num == 2:
        function = new_sum.sum_for_list
    main(function)
