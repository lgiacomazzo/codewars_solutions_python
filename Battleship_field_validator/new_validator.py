from matrix_tests import battleFields


class BattleshipValidatorException(Exception):
    pass


class BattleshipValidator:
    correct_ships_per_size = {
        # length: number of ships
        4: 1,
        3: 2,
        2: 3,
        1: 4
    }

    def __init__(self, battlefield):
        # assuming it's a size*size matrix
        self.battlefield: list[list[int]] = battlefield
        self.size_battlefield = len(self.battlefield)
        # for each size, the position of ships found
        self.battlefield_ships = {}
        self.checked_cells = []

    def find_ship(self, start_row, start_column) -> dict:
        # going from left to right and top to bottom
        # first, check if this position was already visited
        if self.checked_cells[start_row][start_column] == 1:
            return None
        self.checked_cells[start_row][start_column] = 1
        # now check if something is here
        if self.battlefield[start_row][start_column] == 0:
            return None
        # there is something, what ship is it?
        end_row, end_column = start_row, start_column
        size_ship = 1
        # horizontal search first
        for column in range(start_column + 1, self.size_battlefield):
            self.checked_cells[start_row][column] = 1
            if self.battlefield[start_row][column] == 1:
                end_row, end_column = start_row, column
                size_ship += 1
            else:
                break
        # vertical search then, only if size_ship is equal to 1
        if size_ship == 1:
            for row in range(start_row + 1, self.size_battlefield):
                self.checked_cells[row][start_column] = 1
                if self.battlefield[row][start_column] == 1:
                    end_row, end_column = row, start_column
                    size_ship += 1
                else:
                    break
        ship = dict()
        ship["start"] = dict()
        ship["start"]["row"] = start_row
        ship["start"]["column"] = start_column
        ship["end"] = dict()
        ship["end"]["row"] = end_row
        ship["end"]["column"] = end_column
        ship["size"] = size_ship
        return ship

    def initialize(self):
        for key in BattleshipValidator.correct_ships_per_size:
            self.battlefield_ships[key] = []
        self.checked_cells.clear()
        for row in self.battlefield:
            self.checked_cells.append([0] * len(row))

    def check_for_correct_ship(self, ship):
        # check for correct size of ship
        start_coordinates, end_coordinates, size = ship["start"], ship["end"], ship["size"]
        if size not in BattleshipValidator.correct_ships_per_size:
            raise BattleshipValidatorException("Wrong size of ship starting from " +
                                               str(start_coordinates) +
                                               " to " +
                                               str(end_coordinates)
                                               )
        # check for surroundings of ship
        # if ship goes from (4, 3) to (4, 4), then its surrounding go from (3, 2) to (5, 5)
        # if ship goes from (3, 4) to (4, 4), then its surrounding go from (2, 3) to (5, 5)
        for row in range(start_coordinates["row"]-1, end_coordinates["row"]+2):
            if row < 0 or row >= self.size_battlefield:
                continue
            for column in range(start_coordinates["column"]-1, end_coordinates["column"]+2):
                if column < 0 or column >= self.size_battlefield:
                    continue
                # is this cell belonging to the ship? skip
                if (start_coordinates["column"] <= column <= end_coordinates["column"]) \
                        and (start_coordinates["row"] <= row <= end_coordinates["row"]):
                    continue
                # does the cell belong to another ship?
                if self.battlefield[row][column] == 1:
                    raise BattleshipValidatorException("Collision near the ship in position (" +
                                                       str(column) +
                                                       ", " +
                                                       str(row) +
                                                       ")"
                                                       )
        # everything good
        return True

    def check_for_correct_ships(self):
        # check for correct number of ships
        for size, number in BattleshipValidator.correct_ships_per_size.items():
            if len(self.battlefield_ships[size]) != number:
                raise BattleshipValidatorException("Wrong number of ships of length " +
                                                   str(number) +
                                                   ", equal to " +
                                                   str(len(self.battlefield_ships[size]))
                                                   )
        return True

    def validate(self):
        self.initialize()
        # start checking
        try:
            for row in range(self.size_battlefield):
                for column in range(self.size_battlefield):
                    ship = self.find_ship(row, column)
                    if ship is not None:
                        self.check_for_correct_ship(ship)
                        self.battlefield_ships[ship["size"]].append(ship)
            self.check_for_correct_ships()
        except BattleshipValidatorException:
            return False
        return True


def validate_battlefield(battlefield):
    return BattleshipValidator(battlefield).validate()


if __name__ == "__main__":
    for battleField, result in battleFields:
        checking = validate_battlefield(battleField)
        print("Correct test" if checking == result else "Not correct test", "with check = " + str(checking))
