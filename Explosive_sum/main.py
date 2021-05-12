import old_solution.explosive as old_explosive
import new_solution.explosive as new_explosive
from tests.tests import tests


# https://www.codewars.com/kata/52ec24228a515e620b0005ef

def main(explosive):
    for number, result in tests:
        if explosive(number) == result:
            print("ok for " + str(number))
        else:
            print("wrong for " + str(number))


if __name__ == "__main__":
    print("1) No classes")
    print("2) With classes")
    num = int(input("Select one: "))
    explosive = None
    if num == 1:
        explosive = old_explosive.exp_sum
    if num == 2:
        explosive = new_explosive.exp_sum
    main(explosive)
