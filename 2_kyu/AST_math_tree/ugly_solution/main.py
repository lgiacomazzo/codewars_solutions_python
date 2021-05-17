# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


precedence = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "(": 3,
    ")": 3
}

tests = [
["(34) + (-18 + -53 - (49)) * (-20 * -(((-(-59 - -9)))) * -43)", 5160034],
    ["-(-(-1))", -1],
    ["1 + 1", 2],
    ["-7 * -(6 / 3)", 14],
    ["8/16", 0.5],
    ["2 + -2", 0],
    ["10- 2- -5", 13],
    ["(((10)))", 10],
    ["3 * 5", 15],
    ["3 -(-1) -(-1)", 5],
    ["2 + 3 * 4 / 3 - 6 / 3 * 1 + 8", 12],
    ["1 + 2 * 3 * (5 - (3 - 1)) - 8", 11],
    ["5 -1", 4],
    ["2 + 3 * 4 / 3 - 6 / 3 * 3 + 8", 8],
    ["-49 / 40 * -7 - -82 * 80 / 62 * 92 / 4", 2442.123387096774],
    ["-40 - -6 * 4 / -12 + -3 * -3 + 12 - -63", 42.0],
    ["-54 + -27 - 59 - 6 - 59 / -34 - -39 - 45", -150.26470588235293],
    ["61 + 27 - -86 - -18 / 81 - 17 + 64 + -46", 175.22222222222223],
    ["11 / -89 / 94 - 39 / 84 * -71 + -74 + -15", -56.03702913151873],
    ["58 + -10 / 59 - -49 / 12 - 75 - 34 * -43", 1448.9138418079096],
    ["-62 - -65 - 55 * 31 - 67 + 13 + 56 * 44", 708],
    ["-51 * -32 * 51 - 63 / -77 - 38 + -67 / -20", 83198.16818181818],
    ["-56 - 4 * -81 + -52 + 5 * -39 - 96 * 99", -9483],
    ["-34 + 80 - 82 * -23 + 84 + 54 + 22 + 59", 2151],
    ["-45 - -46 - 19 / -41 - -12 / -79 + -88 - -14", -72.68848410003088],
    ["29 - -68 / -17 * -6 + 69 + -86 - -85 / 84", 37.01190476190476],
    ["-87 - 52 / 46 * -98 / 45 * -86 - -51 - -69", -178.71787439613524],
    ["-83 - 58 * -58 - 55 * 27 - -55 + 29 + -99", 1781],
    ["45 - -65 + -76 * -32 - 65 / 76 - 47 - -75", 2569.1447368421054],
    ["85 - 83 * 3 + -16 / 51 - 25 + -79 + -19", -287.3137254901961],
    ["-52 - -17 / -4 + 31 - 1 * 55 + -19 / 69", -80.52536231884058],
    ["85 - -29 - 16 / 76 / 82 - 47 + -72 - -100", 94.997432605905],
    ["91 - -40 / -90 + 41 - -72 / 12 / 35 / 93", 131.5573988735279],
    ["-10 - -36 * 25 * -73 - 10 - -31 * 2 / -82", -65720.75609756098],
    ["48 - 55 * 37 * 34 - -10 + 23 / 8 + -73", -69202.125],
    ["-16 - -67 / -94 - 85 - 7 + 36 * -78 - 6", -2922.7127659574467],
    ["22 - -2 - 2 * -2 - -16 / -10 - -33 - 97", -37.6],
    ["-68 / 77 - 20 * -42 - -4 + -6 / -50 - 13", 830.2368831168832],
    ["-18 + -53 - (49)", -120],
    ["(56) / (56 - -45 * -(89)) * (38 / -(((-(-52 * -1)))) - 8)", 0.10308354598048192],
    ["(94) / (69 + -56 / -(41)) + (100 - -((((-20 - 89)))) * 36)", -3822.6641247833622],
    ["-(-52) * (66 + -15 * -(20)) * (-77 / -(((-(-58 / -10)))) - 7)", -385890.2068965517],
    ["-(26) / (-90 - -11 * -(16)) + (-92 * ((((-26 * -44)))) + -84)", -105331.9022556391],
    ["-(26) * (-42 + -57 * -(30)) * (-5 / -(((-(-8 * -10)))) - 56)", 2431318.5],
    ["(-37) - (-45 + 69 * -(29)) / (-57 + -((((49 - -65)))) * -88)", -36.79488721804511],
    ["(59) + (-40 - -84 / -(81)) - (-83 / ((((-61 + 9)))) / 90)", 17.945227920227918],
    ["-(41) + (34 - 42 / -(74)) - (25 + -((((30 * -36)))) * -56)", 60448.56756756757],
    ["(-3) + (83 - 63 * -(93)) * (48 / (((-(100 + -34)))) + 40)", 233355.54545454547],
    ["(28) / (62 + 89 / -(70)) / (-89 / (((-(-23 * 73)))) / 30)", -260.9437567895459],
    ["(-45) - (73 - 19 * -(43)) * (5 - -(((-(51 + 36)))) - -43)", 34665],
    ["(9) + (89 + -75 * -(90)) * (-36 / -(((-(-35 + 11)))) * -34)", -348780.0]
]

def get_first_number(math_expression):
    first_number = ord("0")
    last_number = ord("9")
    number = ""
    new_expression = math_expression
    while len(new_expression) > 0:
        first_char = new_expression[0]
        # considerare anche il segno meno
        if first_char in ("-") and len(number) == 0:
            number += first_char
        elif first_number <= ord(first_char) <= last_number:
            number += first_char
        else:
            break
        new_expression = new_expression[1:]
    if len(number) == 0 or (number == "-"):
        return None, math_expression
    new_expression = new_expression.lstrip()
    # print("NR: ", (number, new_expression))
    return number, new_expression


def get_first_operator(math_expression):
    operators = ("+", "-", "*", "/", "(", ")")
    operator = ""
    new_expression = math_expression
    if len(new_expression) > 0:
        first_char = new_expression[0]
        if first_char in operators:
            operator = first_char
            new_expression = new_expression[1:]
    if len(operator) == 0:
        return None, math_expression
    new_expression = new_expression.lstrip()
    # print("OP: ", (operator, new_expression))
    return operator, new_expression


def resolve_operations(stack_numbers, stack_operators):
    while len(stack_operators) > 0:
        stack_numbers, stack_operators = resolve_operation(stack_numbers, stack_operators, left_to_right=True)
    return stack_numbers, stack_operators


def resolve_operation(stack_numbers, stack_operators, left_to_right=False):
    global precedence
    if len(stack_operators) == 0:
        return stack_numbers, stack_operators

    if left_to_right is False:
        current_operator = stack_operators.pop()
    else:
        current_operator = stack_operators[0]
        stack_operators = stack_operators[1:]
    if current_operator == "*":
        if left_to_right is False:
            second_number = stack_numbers.pop()
            first_number = stack_numbers.pop()
            stack_numbers.append(first_number * second_number)
        else:
            second_number = stack_numbers[1]
            first_number = stack_numbers[0]
            stack_numbers = stack_numbers[2:]
            stack_numbers.insert(0, first_number * second_number)

    elif current_operator == "/":
        if left_to_right is False:
            second_number = stack_numbers.pop()
            first_number = stack_numbers.pop()
            stack_numbers.append(first_number / second_number)
        else:
            second_number = stack_numbers[1]
            first_number = stack_numbers[0]
            stack_numbers = stack_numbers[2:]
            stack_numbers.insert(0, first_number / second_number)
    elif current_operator == "+":
        if left_to_right is False:
            second_number = stack_numbers.pop()
            first_number = stack_numbers.pop()
            stack_numbers.append(first_number + second_number)
        else:
            second_number = stack_numbers[1]
            first_number = stack_numbers[0]
            stack_numbers = stack_numbers[2:]
            stack_numbers.insert(0, first_number + second_number)
    elif current_operator == "-":
        if left_to_right is False:
            second_number = stack_numbers.pop()
            first_number = stack_numbers.pop()
            stack_numbers.append(first_number - second_number)
        else:
            second_number = stack_numbers[1]
            first_number = stack_numbers[0]
            stack_numbers = stack_numbers[2:]
            stack_numbers.insert(0, first_number - second_number)
    else:
        return stack_numbers, stack_operators
    if len(stack_operators) > 0:
        if left_to_right is False:
            if precedence[current_operator] <= precedence[stack_operators[-1]]:
                return resolve_operation(stack_numbers, stack_operators, left_to_right)
        else:
            if precedence[current_operator] <= precedence[stack_operators[0]]:
                return resolve_operation(stack_numbers, stack_operators, left_to_right)
    return stack_numbers, stack_operators


def reduce_parenthesis(expression_with_par):
    global precedence
    stack_operators = []
    stack_numbers = []
    new_expression = expression_with_par
    couple_end = False
    couple_start = False
    at_least_one_operator = False
    number_last_time = False
    default_max_precedence = 99999999999999
    lowest_precedence = default_max_precedence
    while len(new_expression) > 0 and not couple_end:
        number, new_expression = get_first_number(new_expression)
        if number is not None:
            stack_numbers.append(int(number))
            if number_last_time is True:
                lowest_precedence = lowest_precedence if lowest_precedence < precedence["+"] else precedence["+"]
                stack_operators.append("+")
            else:
                number_last_time = True
            continue
        # no numbers found
        operator, new_expression = get_first_operator(new_expression)
        if operator is not None:
            number_last_time = False

            if len(stack_operators) > 0:
                last_operator = stack_operators[-1]
                if precedence[last_operator] >= precedence[operator] and precedence[last_operator] > lowest_precedence and len(stack_numbers) > len(stack_operators):
                    stack_numbers, stack_operators = resolve_operation(stack_numbers, stack_operators)
                    if len(stack_operators) == 0:
                        lowest_precedence = default_max_precedence
            if operator == '(':
                if couple_start is False:
                    couple_start = True
                else:
                    value_computed, new_expression = reduce_parenthesis(operator + new_expression)
                    if not at_least_one_operator and (len(stack_operators) > 0 or len(stack_numbers) > 0):
                        lowest_precedence = lowest_precedence if lowest_precedence < precedence["+"] else precedence["+"]
                        stack_operators.append("+")
                    elif len(stack_operators) > len(stack_numbers):
                        # assuming syntax is correct, this means that a + or - is referred to the () pars, when an operator already exists before that
                        # for example 5 * -(2)
                        new_operator = stack_operators.pop()
                        if new_operator == "-":
                            value_computed = -value_computed
                        elif new_operator == "+":
                            pass
                        else:
                            print("Problem")
                    stack_numbers.append(value_computed)
                    at_least_one_operator = False
            elif operator == ')':
                couple_end = True
            else:
                at_least_one_operator = True
                lowest_precedence = lowest_precedence if lowest_precedence < precedence[operator] else precedence[operator]
                stack_operators.append(operator)
            continue
        break
    # possibile che un operatore a piu' alta priorità sia vivo alla fine
    if len(stack_operators) > 1:
        last_operator = stack_operators[-1]
        second_to_last_operator = stack_operators[-2]
        if precedence[last_operator] > precedence[second_to_last_operator]:
            # print("Precedence: ", last_operator, operator)
            stack_numbers, stack_operators = resolve_operation(stack_numbers, stack_operators)
    # sono tutti operatori con la stessa precedenza --> solo da sinistra a destra
    stack_numbers, stack_operators = resolve_operations(stack_numbers, stack_operators)
    return stack_numbers.pop(), new_expression  # evaluated expression


def calc(math_expression):
    global precedence
    print(math_expression)
    stack_operators = []
    stack_numbers = []
    at_least_one_operator = False
    number_last_time = False
    default_max_precedence = 99999999999999
    lowest_precedence = default_max_precedence
    new_expression = math_expression
    while len(new_expression) > 0:
        number, new_expression = get_first_number(new_expression)
        if number is not None:
            stack_numbers.append(int(number))
            if number_last_time is True:
                lowest_precedence = lowest_precedence if lowest_precedence < precedence["+"] else precedence["+"]
                stack_operators.append("+")
            else:
                number_last_time = True
            continue
        # no numbers found
        operator, new_expression = get_first_operator(new_expression)
        if operator is not None:
            number_last_time = False
            if len(stack_operators) > 0 and not (operator == '-' and get_first_operator(new_expression)[0] == '('):
                last_operator = stack_operators[-1]
                if precedence[last_operator] >= precedence[operator] and precedence[last_operator] > lowest_precedence and len(stack_numbers) > len(stack_operators):
                    # print("Precedence: ", last_operator, operator)
                    stack_numbers, stack_operators = resolve_operation(stack_numbers, stack_operators)
                    if len(stack_operators) == 0:
                        lowest_precedence = default_max_precedence
            if operator == '(':
                value_computed, new_expression = reduce_parenthesis(operator + new_expression)
                if not at_least_one_operator and (len(stack_operators) > 0 or len(stack_numbers) > 0):
                    lowest_precedence = lowest_precedence if lowest_precedence < precedence["+"] else precedence["+"]
                    stack_operators.append("+")
                elif len(stack_operators) > len(stack_numbers):
                    # assuming syntax is correct, this means that a + or - is referred to the () pars, when an operator already exists before that
                    # for example 5 * -(2)
                    new_operator = stack_operators.pop()
                    if new_operator == "-":
                        value_computed = -value_computed
                    elif new_operator == "+":
                        pass
                    else:
                        print("Problem")
                stack_numbers.append(value_computed)
                at_least_one_operator = False
            else:
                at_least_one_operator = True
                lowest_precedence = lowest_precedence if lowest_precedence < precedence[operator] else precedence[operator]
                stack_operators.append(operator)
            continue
        # no operators found (wrong formula, should never come here)
        break
    # possibile che un operatore a piu' alta priorità sia vivo alla fine
    if len(stack_operators) > 1:
        last_operator = stack_operators[-1]
        second_to_last_operator = stack_operators[-2]
        if precedence[last_operator] > precedence[second_to_last_operator]:
            # print("Precedence: ", last_operator, operator)
            stack_numbers, stack_operators = resolve_operation(stack_numbers, stack_operators)

    # sono tutti operatori con la stessa precedenza --> solo da sinistra a destra
    stack_numbers, stack_operators = resolve_operations(stack_numbers, stack_operators)
    return stack_numbers.pop()  # evaluated expression


if __name__ == '__main__':
    index = 0
    for expression, result in tests:
        index += 1
        try:
            print("------------ Next -------------")
            result_obtained = calc(expression)
            if result_obtained == result:
                continue
                # print(result_obtained, "->", result)
            else:
                print(str(index) + " - Ottenuto " + str(result_obtained) + ", ma dovevo ottenere " + str(result))
        except:
            print(str(index) + ": AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa")
