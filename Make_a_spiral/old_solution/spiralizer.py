def spiralize(size):
    spiral = [[0 for i in range(size)] for i in range(size)]
    row = column = 0
    lines = 0
    counter = 0
    while True:
        # right
        if lines == size:
            break
        while column < size - (counter << 1):
            spiral[row][column] = 1
            if column == size - 1:
                break
            # look right and down
            if (spiral[row + 1][column] == 1 or spiral[row][column + 1] == 1):
                spiral[row][column] = 0
                column -= 1
                break
            else:
                column += 1

        if column == size - (counter << 1):
            column -= 1
        row += 1
        lines += 1

        # down
        if lines == size:
            break
        while row < size - (counter << 1):
            spiral[row][column] = 1
            if row == size - 1:
                break
            # look down and left
            if (spiral[row + 1][column] == 1 or spiral[row][column - 1] == 1):
                spiral[row][column] = 0
                row -= 1
                break
            else:
                row += 1

        if row == size - (counter << 1):
            row -= 1
        column -= 1
        lines += 1

        # left
        if lines == size:
            break
        while column >= (counter << 1):
            spiral[row][column] = 1

            if column == 0:
                break
            # look left and up
            if (spiral[row - 1][column] == 1 or spiral[row][column - 1] == 1):
                spiral[row][column] = 0
                column += 1
                break
            else:
                column -= 1

        if column < (counter << 1):
            column += 1
        row -= 1
        lines += 1

        # up
        if lines == size:
            break
        while row >= (counter << 1):
            spiral[row][column] = 1

            if row == 0:
                break
            # look up and right
            if (spiral[row - 1][column] == 1 or spiral[row][column + 1] == 1):
                spiral[row][column] = 0
                row += 1
                break
            else:
                row -= 1

        if row < (counter << 1):
            row += 1
        column += 1
        lines += 1
        # new round
        counter += 1
    return spiral

