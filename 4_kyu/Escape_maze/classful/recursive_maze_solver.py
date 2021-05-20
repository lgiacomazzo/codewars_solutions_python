from .base_maze_solver import BaseMazeSolver

class RecursiveMazeSolver(BaseMazeSolver):

    def __init__(self, maze):
        super().__init__(maze)

    def recursive_escape(self, position):
        # first check our position
        valid_position, end_of_maze = self.control_for_each_step(position)
        if not valid_position:
            # not correct char
            return None
        row, column, _ = position
        self.maze[row][column] = "0"
        if end_of_maze:
            # reached the end
            return []
        # move only forward, left, and right. No moving backwards
        # move forward first
        stack_moves = []
        successive_moves = self.recursive_escape(self.move_forward(position))
        if successive_moves is not None:
            stack_moves += "F"
            stack_moves += successive_moves
            # print("Found a route: forward")
            return stack_moves
        # move left
        successive_moves = self.recursive_escape(self.move_left(position))
        if successive_moves is not None:
            stack_moves += "L"
            stack_moves += "F"
            stack_moves += successive_moves
            # print("Found a route: left")
            return stack_moves
        # move right
        successive_moves = self.recursive_escape(self.move_right(position))
        if successive_moves is not None:
            stack_moves += "R"
            stack_moves += "F"
            stack_moves += successive_moves
            # print("Found a route: right")
            return stack_moves
        return None

    def escape(self):
        return super().escape(escape_func=self.recursive_escape)