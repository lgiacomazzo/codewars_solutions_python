def move(start_position, direction):
    if direction not in ["forward", "backwards", "left", "right"]:
        raise Exception("Not correct direction: {dir}".format(dir=direction))
    row, column, char = start_position
    row_change, column_change, new_char = movements[char][direction]
    return [row + row_change, column + column_change, new_char]


def move_left(start_position):
    return move(start_position, "left")


def move_right(start_position):
    return move(start_position, "right")


def move_forward(start_position):
    return move(start_position, "forward")


def move_backwards(start_position):
    return move(start_position, "backwards")

movements = {
    # char: direction: (row_change, column_change, direction)
    ">": {
        "forward": (0, +1, ">"),
        "backwards": (0, -1, "<"),
        "left": (-1, 0, "^"),
        "right": (+1, 0, "v")
    },
    "<": {
        "forward": (0, -1, "<"),
        "backwards": (0, +1, ">"),
        "left": (+1, 0, "v"),
        "right": (-1, 0, "^")
    },
    "^": {
        "forward": (-1, 0, "^"),
        "backwards": (+1, 0, "v"),
        "left": (0, -1, "<"),
        "right": (0, +1, ">")
    },
    "v": {
        "forward": (+1, 0, "v"),
        "backwards": (-1, 0, "^"),
        "left": (0, +1, ">"),
        "right": (0, -1, "<")
    }
}


def print_maze(maze):
    print("-------------")
    for row in maze:
        print(row)
    print("-------------")


def control_for_each_step(maze, position):
    """
    :param maze:
    :param position:
    :return: two booleans, first is True if the current position is valid (is ' ', not '#')
    second is True if the current position is located on the edge of the maze
    """
    # return: valid_position, end_of_maze
    row, column, char = position
    # valid character
    valid_position = maze[row][column] != "#"
    # end of maze
    end_of_maze = \
        row == 0 or row == len(maze) - 1 or \
        column == 0 or column == len(maze[0]) - 1
    return valid_position, end_of_maze

def find_start_position(formatted_maze):
    # 1) find the starting position and rotation
    start_position = None
    row_index = 0
    for row in formatted_maze:
        column_index = 0
        for char in row:
            if char in "<>^v":
                start_position = [row_index, column_index, char]
                break
            column_index += 1
        if start_position is not None:
            break
        row_index += 1
    return start_position
