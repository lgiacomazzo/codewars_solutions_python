class Spiralizer:

    def __init__(self, size):
        self.size = size
        self.current_position = (0, 0)
        self.stopped = False
        self.matrix = []

    def initialize(self):
        self.stopped = False
        self.current_position = (0, 0)
        self.matrix.clear()
        self.matrix = [[0] * self.size for _ in range(self.size)]

    def go_right(self):
        column, row = self.current_position
        at_least_one = False
        # update position (and set to 1)
        for x in range(column+1, self.size):
            # next position and its down side
            if self.matrix[row][x] == 1 or self.matrix[row+1][x] == 1:
                break
            self.matrix[row][column] = 1
            column += 1
            at_least_one = True

        if column == self.size - 1:
            self.matrix[row][column] = 1
        elif at_least_one:
            column -= 1

        self.stopped = self.current_position == (column, row)
        self.current_position = (column, row)

    def go_down(self):
        column, row = self.current_position
        at_least_one = False
        # update position (and set to 1)
        for y in range(row+1, self.size):
            # next position and its left side
            if self.matrix[y][column] == 1 or self.matrix[y][column-1] == 1:
                break
            self.matrix[row][column] = 1
            row += 1
            at_least_one = True

        if row == self.size - 1:
            self.matrix[row][column] = 1
        elif at_least_one:
            row -= 1

        self.stopped = self.current_position == (column, row)
        self.current_position = (column, row)

    def go_left(self):
        column, row = self.current_position
        at_least_one = False
        # update position (and set to 1)
        for x in range(column-1, -1, -1):
            # next position and its up side
            if self.matrix[row][x] == 1 or self.matrix[row-1][x] == 1:
                break
            self.matrix[row][column] = 1
            column -= 1
            at_least_one = True

        if column == 0:
            self.matrix[row][column] = 1
        elif at_least_one:
            column += 1

        self.stopped = self.current_position == (column, row)
        self.current_position = (column, row)

    def go_up(self):
        column, row = self.current_position
        at_least_one = False
        # update position (and set to 1)
        for y in range(row-1, -1, -1):
            # next position and its right side
            if self.matrix[y][column] == 1 or self.matrix[y][column+1] == 1:
                break
            self.matrix[row][column] = 1
            row -= 1
            at_least_one = True

        # row will always be > 0
        if at_least_one:
            row += 1

        self.stopped = self.current_position == (column, row)
        self.current_position = (column, row)

    def spiralize(self):
        self.initialize()
        while not self.stopped:
            self.go_right()
            self.go_down()
            self.go_left()
            self.go_up()
        return self.matrix


def spiralize(number):
    return Spiralizer(number).spiralize()
