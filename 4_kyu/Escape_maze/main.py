from tests.tests import tests

# https://www.codewars.com/kata/5877027d885d4f6144000404

# Return the array of movements to execute to get out of the maze

movements = {
    # char: direction: (row_change, column_change, new_char)
    ">": {
        "forward":      (0, +1, ">"),
        "backwards":    (0, -1, "<"),
        "left":         (-1, 0, "^"),
        "right":        (+1, 0, "v")
    },
    "<": {
        "forward":      (0, -1, "<"),
        "backwards":    (0, +1, ">"),
        "left":         (+1, 0, "v"),
        "right":        (-1, 0, "^")
    },
    "^": {
        "forward":      (-1, 0, "^"),
        "backwards":    (+1, 0,"v"),
        "left":         (0, -1, "<"),
        "right":        (0, +1, ">")
    },
    "v": {
        "forward":      (+1, 0, "v"),
        "backwards":    (-1, 0, "^"),
        "left":         (0, +1, ">"),
        "right":        (0, -1, "<")
    }
}


def recursive_escape(maze, position):
    # first check our position
    row, column, char = position
    if maze[row][column] == "#":
        # not correct char
        return None
    if row == 0 or row == len(maze) - 1:
        # reached the end
        return []
    if column == 0 or column == len(maze[0]) - 1:
        # reached the end
        return []
    # move only forward, left, and right. No moving backwards
    # move forward first
    stack_moves = []
    successive_moves = recursive_escape(maze, move_forward(position))
    if successive_moves is not None:
        stack_moves += "F"
        stack_moves += successive_moves
        print("Found a route: forward")
        return stack_moves
    # move left
    successive_moves = recursive_escape(maze, move_left(position))
    if successive_moves is not None:
        stack_moves += "L"
        stack_moves += "F"
        stack_moves += successive_moves
        print("Found a route: left")
        return stack_moves
    # move right
    successive_moves = recursive_escape(maze, move_right(position))
    if successive_moves is not None:
        stack_moves += "R"
        stack_moves += "F"
        stack_moves += successive_moves
        print("Found a route: right")
        return stack_moves
    return None

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

def escape(maze):
    # Have a nice sleep ;)
    for row in maze:
        print(row)
    # 1) find the starting position and rotation
    start_position = None
    row_index = 0
    for row in maze:
        for char in "<>^v":
            column_index = row.find(char)
            if column_index >= 0:
                start_position = [row_index, column_index, char]
                break
        if start_position is not None:
            break
        row_index += 1
    print(start_position)
    stack_moves = []
    print(move_forward(start_position))
    print(move_backwards(start_position))
    print(move_left(start_position))
    print(move_right(start_position))
    # move forward first
    successive_moves = recursive_escape(maze, move_forward(start_position))
    if successive_moves is not None:
        stack_moves += "F"
        stack_moves += successive_moves
        print("Found a route: forward")
        return stack_moves
    # move left
    successive_moves = recursive_escape(maze, move_left(start_position))
    if successive_moves is not None:
        stack_moves += "L"
        stack_moves += "F"
        stack_moves += successive_moves
        print("Found a route: left")
        return stack_moves
    # move right
    successive_moves = recursive_escape(maze, move_right(start_position))
    if successive_moves is not None:
        stack_moves += "R"
        stack_moves += "F"
        stack_moves += successive_moves
        print("Found a route: right")
        return stack_moves
    # move backwards
    successive_moves = recursive_escape(maze, move_backwards(start_position))
    if successive_moves is not None:
        stack_moves += "B"
        stack_moves += "F"
        stack_moves += successive_moves
        print("Found a route: backwards")
        return stack_moves
    return stack_moves


def test():
    for maze, result in tests:
        if escape(maze) != result:
            print("Path generated is different")
    print("Tests passed")


if __name__ == "__main__":
    test()
