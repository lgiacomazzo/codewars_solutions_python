from tests.tests import tests
import re

# https://www.codewars.com/kata/58924f2ca8c628f21a0001a1


def optimize_code(source_code):
    modified_source_code = source_code
    useless_chars = "<>|><|\+\-|\-\+|\[\]|[^+-<>,\[\]]"
    while True:
        modified_source_code = re.sub(useless_chars, "", modified_source_code)
        if len(modified_source_code) == len(source_code):
            return modified_source_code
        source_code = modified_source_code


def generate_c_code(source_code):
    c_code = ""
    list_symbols = re.findall("\++|-+|>+|<+|\.|,|\[|\]", source_code)
    indent = 0
    indent_space = " " * 2
    for symbol in list_symbols:
        if symbol.startswith("+"):
            c_code += indent_space * indent
            c_code += "*p += {number};\n".format(number=len(symbol))
        elif symbol.startswith("-"):
            c_code += indent_space * indent
            c_code += "*p -= {number};\n".format(number=len(symbol))
        elif symbol.startswith("<"):
            c_code += indent_space * indent
            c_code += "p -= {number};\n".format(number=len(symbol))
        elif symbol.startswith(">"):
            c_code += indent_space * indent
            c_code += "p += {number};\n".format(number=len(symbol))
        elif symbol.startswith(","):
            c_code += indent_space * indent
            c_code += "*p = getchar();\n"
        elif symbol.startswith("."):
            c_code += indent_space * indent
            c_code += "putchar(*p);\n"
        elif symbol.startswith("["):
            c_code += indent_space * indent
            c_code += "if (*p) do {\n"
            indent += 1
        elif symbol.startswith("]"):
            indent -= 1
            c_code += indent_space * indent
            c_code += "} while (*p);\n"
    return c_code


def check_for_errors(source_code):
    stack_par = []
    try:
        for symbol in source_code:
            if symbol == "[":
                stack_par.append(0)
            elif symbol == "]":
                stack_par.pop()
    except IndexError:
        # more ] than [
        return True
    if len(stack_par) > 0:
        # more [ than ]
        return True
    return False


def brainfuck_to_c(source_code):
    # 1
    optimized_source_code = optimize_code(source_code)
    # 2
    if check_for_errors(optimized_source_code):
        return "Error!"
    # 3
    c_code = generate_c_code(optimized_source_code)
    return c_code


def test():
    for code, c_code in tests:
        if brainfuck_to_c(code) != c_code:
            print("Code generated is different")
    print("Tests passed")


if __name__ == "__main__":
    test()
