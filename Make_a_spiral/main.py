import old_solution.spiralizer as old_spiralizer
import new_solution.spiralizer as new_spiralizer
from tests.tests import tests

# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6

def main(spiralize):
    for number, result in tests:
        if spiralize(number) == result:
            print("ok for " + str(number))
        else:
            print("wrong for " + str(number))

if __name__ == "__main__":
    print("1) No classes")
    print("2) With classes")
    num = int(input("Select one: "))
    spiralize = None
    if num == 1:
        spiralize = old_spiralizer.spiralize
    if num == 2:
        spiralize = new_spiralizer.spiralize
    main(spiralize)
