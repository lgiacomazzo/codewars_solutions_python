# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7
from matrix_tests import battleFields


def check_diagonals(field, row, column):
    if column < len(field) - 1 and row < len(field) - 1:
        if (row == 0 or column == 0):
            if field[row + 1][column + 1] == 1:
                #print("Conflict in perimeter!")
                # solo basso a destra
                return True
        else:
            #print("Looking in inner matrix")
            if field[row + 1][column + 1] == 1 or field[row - 1][column + 1] == 1 or field[row + 1][column - 1] == 1 or \
                    field[row - 1][column - 1] == 1:
                return True
    return False


def check_ship(field, visited, i, j):
    # controllo la lunghezza della nave
    #print(i, j)
    if i == len(field) or j == len(field):
        return 0
    visited[i][j] = 1
    # look
    if field[i][j] == 1:
        #print("Found a ship: ", i, j)
        # ultima riga e/o colonna
        if i == len(field) - 1 and j == len(field) - 1:
            return 1
        if i == len(field) - 1:
            return check_ship(field, visited, i, j + 1) + 1
        if j == len(field) - 1:
            return check_ship(field, visited, i + 1, j) + 1
        # non ultima riga e/o colonna
        if check_diagonals(field, i, j):
            # contatto con una nave
            #print("Conflict found!")
            return -len(field)
        # diagonali libere. Controllo le verticali
        # NB: se supero questo punto, allora assumo di avere solo navi verticali
        # NB2: ogni volta parto dal primo blocco con questo metodo di visita
        if field[i + 1][j] == 1 and field[i][j + 1] == 1:
            # bad case
            return -len(field)
        if field[i + 1][j] == 1:
            return check_ship(field, visited, i + 1, j) + 1
        elif field[i][j + 1] == 1:
            return check_ship(field, visited, i, j + 1) + 1
        else:
            return 1
    return 0


def validate_battlefield(field):
    # devono esserci 20 1 nella matrice
    # tutti in linea
    # niente blocchi nel dintorno, tranne il continuo della nave
    len_field = len(field)
    range_field = range(len_field)
    if sum(field[i].count(1) for i in range_field) != 20:
        return False
    visited = [[0 for i in range_field] for i in range_field]
    list_ships = [0, 0, 0, 0]
    list_correct_ships = [4, 3, 2, 1]
    # visito da sinistra a destra, dall'alto verso il basso
    # eccezione: trovo una nave
    for i in range_field:
        for j in range_field:
            if visited[i][j] == 1:
                continue
            len_ship = check_ship(field, visited, i, j)
            if len_ship < 0 or len_ship > 4:
                return False
            if len_ship == 0:
                continue
            # da 1 a 4
            #print("length ship: " + str(len_ship))
            list_ships[len_ship - 1] += 1
    #print(list_ships, list_correct_ships)
    if list_ships[0:] == list_correct_ships[0:]:
        return True
    return False



if __name__ == "__main__":
    for battleField, result in battleFields:
        checking = validate_battlefield(battleField)
        print("Correct test" if checking == result else "Not correct test", "with check = " + str(checking))