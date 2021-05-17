from itertools import permutations, combinations
from tests.tests import tests


# https://www.codewars.com/kata/57cebf1472f98327760003cd

def determinant(p1, p2, p3):
    # point[0] is the x axis, point[1] is the y axis
    return p1[0] * p2[1] * 1 + p1[1] * 1 * p3[0] + 1 * p2[0] * p3[1] - (
            p1[0] * 1 * p3[1] + p1[1] * p2[0] * 1 + 1 * p2[1] * p3[0])


def count_col_triangle(input_):
    # your code here
    separation_dict = {}
    for point, color in input_:
        if color not in separation_dict:
            separation_dict[color] = []
        separation_dict[color].append(point)
    color_dict = {}
    func = permutations
    for color in separation_dict:
        color_dict[color] = 0
        if len(separation_dict[color]) < 3:
            continue

        for p1, p2, p3 in func(separation_dict[color], 3):
            if determinant(p1, p2, p3) > 0:
                color_dict[color] += 1

    for color in color_dict:
        # in this way each triangle will be counted three times
        color_dict[color] //= 3
    print(separation_dict)
    print(color_dict)
    total_points = len(input_)
    total_colors = len(color_dict)
    total_possible_triangles = sum(color_dict[color] for color in color_dict)
    list_colors = []
    max_colors = 0
    for color in sorted(color_dict):
        if color_dict[color] > max_colors:
            list_colors.clear()
        if color_dict[color] >= max_colors:
            max_colors = color_dict[color]
            list_colors.append(color)
    if max_colors == 0:
        list_colors.clear()
    else:
        list_colors.append(max_colors)
    final_result = [total_points, total_colors, total_possible_triangles, list_colors]
    return final_result


def main():
    for input_, result in tests:
        print("Next")
        returned_result = count_col_triangle(input_)
        if returned_result != result:
            raise Exception("Different result, this was required: " +
                            str(result) +
                            ", and this was obtained: " +
                            str(returned_result)
                            )
    print("Tests passed")


if __name__ == "__main__":
    main()
