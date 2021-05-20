class BaseMazeSolver:
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

    def __init__(self, maze):
        self.maze = [[char for char in string] for string in maze]

    @staticmethod
    def print_maze(maze):
        print("-------------")
        for row in maze:
            print(row)
        print("-------------")

    def control_for_each_step(self, position):
        """
        :param position:
        :return: two booleans, first is True if the current position is valid (is ' ', not '#')
        second is True if the current position is located on the edge of the maze
        """
        # return: valid_position, end_of_maze
        row, column, char = position
        valid_position = self.maze[row][column] != "#"
        # end of maze
        end_of_maze = \
            row == 0 or row == len(self.maze) - 1 or \
            column == 0 or column == len(self.maze[0]) - 1
        return valid_position, end_of_maze

    def move(self, start_position, direction):
        if direction not in ["forward", "backwards", "left", "right"]:
            raise Exception("Not correct direction: {dir}".format(dir=direction))
        row, column, char = start_position
        row_change, column_change, new_char = BaseMazeSolver.movements[char][direction]
        return [row + row_change, column + column_change, new_char]

    def move_left(self, start_position):
        return self.move(start_position, "left")

    def move_right(self, start_position):
        return self.move(start_position, "right")

    def move_forward(self, start_position):
        return self.move(start_position, "forward")

    def move_backwards(self, start_position):
        return self.move(start_position, "backwards")

    def find_start_position(self):
        # 1) find the starting position and rotation
        start_position = None
        row_index = 0
        for row in self.maze:
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

    def escape(self, escape_func):
        start_position = self.find_start_position()
        stack_moves = []
        try:
            successive_moves = escape_func(self.move_forward(start_position))
            if successive_moves is not None:
                stack_moves += "F"
                for move in successive_moves:
                    stack_moves += move
                # print("Found a route: forward")
                raise Exception("over")
            # move left
            successive_moves = escape_func(self.move_left(start_position))
            if successive_moves is not None:
                stack_moves += "L"
                stack_moves += "F"
                for move in successive_moves:
                    stack_moves += move
                # print("Found a route: left")
                raise Exception("over")
            # move right
            successive_moves = escape_func(self.move_right(start_position))
            if successive_moves is not None:
                stack_moves += "R"
                stack_moves += "F"
                for move in successive_moves:
                    stack_moves += move
                # print("Found a route: right")
                raise Exception("over")
            # move backwards
            successive_moves = escape_func(self.move_backwards(start_position))
            if successive_moves is not None:
                stack_moves += "B"
                stack_moves += "F"
                for move in successive_moves:
                    stack_moves += move
                # print("Found a route: backwards")
                raise Exception("over")
        except Exception:
            pass
        return stack_moves