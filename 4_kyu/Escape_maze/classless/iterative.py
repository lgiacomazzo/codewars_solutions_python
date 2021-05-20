from .common import move_right, move_left, move_forward, move_backwards, control_for_each_step, find_start_position


def iterative_escape(maze, position):
    """
    Tralasciando la primissima cella, tutte le altre possono visitare le celle vicine tranne
    quella da cui provengono. Tecnica DFS. In questo caso, nel path conservo una sequenza di liste
    ciascuna rappresentanti un percorso fino ad un incrocio (due o tre alternative, esclusa la strada
    percorsa). Ogni volta che viene trovato un incrocio, il path attuale viene salvato in uno stack,
    e il path viene svuotato, e riempito con i comandi necessari alla visita (es: prima mi muovo in
    avanti, quindi path conterrà solo "F"). Se il percorso non ha esito positivo, basta rimuovere
    il path conservato più recentemente nello stack
    :param maze:
    :param position:
    :return:
    """

    stack_moves = [(position, None)]
    # move only forward, left, and right. No moving backwards
    # move forward first
    path = []
    while len(stack_moves) > 0:
        current_position, commands = stack_moves.pop()
        valid_position, end_of_maze = control_for_each_step(maze, current_position)
        row, column, char = current_position
        if commands is not None and commands[0] == "B":
            path.pop()
            continue
        if not valid_position:
            # cosa devo fare quando non ho una posizione valida? devo annullare l'ultima mossa fatta
            continue
        path.append(commands)
        maze[row][column] = "0"
        if end_of_maze:
            break
        stack_moves.append((current_position, ["B"]))
        stack_moves.append((move_left(current_position), ["L", "F"]))
        stack_moves.append((move_right(current_position), ["R", "F"]))
        stack_moves.append((move_forward(current_position), ["F"]))
    if len(path) > 0:
        # a path is found. Remove the command None though (used only for internal behaviour)
        path.pop(0)
        return path
    else:
        return None


def escape(maze):
    # Have a nice sleep ;)
    formatted_maze = [[char for char in string] for string in maze]
    start_position = find_start_position(formatted_maze)
    stack_moves = []
    # print(move_forward(start_position))
    # print(move_backwards(start_position))
    # print(move_left(start_position))
    # print(move_right(start_position))
    # move forward first
    try:
        successive_moves = iterative_escape(formatted_maze, move_forward(start_position))
        if successive_moves is not None:
            stack_moves += "F"
            for move in successive_moves:
                stack_moves += move
            # print("Found a route: forward")
            raise Exception("over")
        # move left
        successive_moves = iterative_escape(formatted_maze, move_left(start_position))
        if successive_moves is not None:
            stack_moves += "L"
            stack_moves += "F"
            for move in successive_moves:
                stack_moves += move
            # print("Found a route: left")
            raise Exception("over")
        # move right
        successive_moves = iterative_escape(formatted_maze, move_right(start_position))
        if successive_moves is not None:
            stack_moves += "R"
            stack_moves += "F"
            for move in successive_moves:
                stack_moves += move
            # print("Found a route: right")
            raise Exception("over")
        # move backwards
        successive_moves = iterative_escape(formatted_maze, move_backwards(start_position))
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
