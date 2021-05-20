from .common import move_left, move_right, move_forward, move_backwards, control_for_each_step, find_start_position


def recursive_escape(maze, position):
    # first check our position
    valid_position, end_of_maze = control_for_each_step(maze, position)
    if not valid_position:
        # not correct char
        return None
    row, column, _ = position
    maze[row][column] = "0"
    if end_of_maze:
        # reached the end
        return []
    # move only forward, left, and right. No moving backwards
    # move forward first
    stack_moves = []
    successive_moves = recursive_escape(maze, move_forward(position))
    if successive_moves is not None:
        stack_moves += "F"
        stack_moves += successive_moves
        # print("Found a route: forward")
        return stack_moves
    # move left
    successive_moves = recursive_escape(maze, move_left(position))
    if successive_moves is not None:
        stack_moves += "L"
        stack_moves += "F"
        stack_moves += successive_moves
        # print("Found a route: left")
        return stack_moves
    # move right
    successive_moves = recursive_escape(maze, move_right(position))
    if successive_moves is not None:
        stack_moves += "R"
        stack_moves += "F"
        stack_moves += successive_moves
        # print("Found a route: right")
        return stack_moves
    return None


def escape(maze):
    # Have a nice sleep ;)
    formatted_maze = [[char for char in string] for string in maze]
    start_position = find_start_position(formatted_maze)
    # print(start_position)
    stack_moves = []
    # print(move_forward(start_position))
    # print(move_backwards(start_position))
    # print(move_left(start_position))
    # print(move_right(start_position))
    # move forward first
    successive_moves = recursive_escape(formatted_maze, move_forward(start_position))
    if successive_moves is not None:
        stack_moves += "F"
        stack_moves += successive_moves
        # print("Found a route: forward")
        return stack_moves
    # move left
    successive_moves = recursive_escape(formatted_maze, move_left(start_position))
    if successive_moves is not None:
        stack_moves += "L"
        stack_moves += "F"
        stack_moves += successive_moves
        # print("Found a route: left")
        return stack_moves
    # move right
    successive_moves = recursive_escape(formatted_maze, move_right(start_position))
    if successive_moves is not None:
        stack_moves += "R"
        stack_moves += "F"
        stack_moves += successive_moves
        # print("Found a route: right")
        return stack_moves
    # move backwards
    successive_moves = recursive_escape(formatted_maze, move_backwards(start_position))
    if successive_moves is not None:
        stack_moves += "B"
        stack_moves += "F"
        stack_moves += successive_moves
        # print("Found a route: backwards")
        return stack_moves
    return stack_moves
