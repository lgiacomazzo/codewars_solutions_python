from .base_maze_solver import BaseMazeSolver

class IterativeMazeSolver(BaseMazeSolver):

    def __init__(self, maze):
        super().__init__(maze)

    def iterative_escape(self, position):
        """
        Tralasciando la primissima cella, tutte le altre possono visitare le celle vicine tranne
        quella da cui provengono. Tecnica DFS. In questo caso, nel path conservo una sequenza di liste
        ciascuna rappresentanti un percorso fino ad un incrocio (due o tre alternative, esclusa la strada
        percorsa). Ogni volta che viene trovato un incrocio, il path attuale viene salvato in uno stack,
        e il path viene svuotato, e riempito con i comandi necessari alla visita (es: prima mi muovo in
        avanti, quindi path conterrà solo "F"). Se il percorso non ha esito positivo, basta rimuovere
        il path conservato più recentemente nello stack
        :param position:
        :return:
        """

        stack_moves = [(position, None)]
        # move only forward, left, and right. No moving backwards
        # move forward first
        path = []
        while len(stack_moves) > 0:
            current_position, commands = stack_moves.pop()
            valid_position, end_of_maze = self.control_for_each_step(current_position)
            row, column, char = current_position
            if commands is not None and commands[0] == "B":
                path.pop()
                continue
            if not valid_position:
                # cosa devo fare quando non ho una posizione valida? devo annullare l'ultima mossa fatta
                continue
            path.append(commands)
            self.maze[row][column] = "0"
            if end_of_maze:
                break
            stack_moves.append((current_position, ["B"]))
            stack_moves.append((self.move_left(current_position), ["L", "F"]))
            stack_moves.append((self.move_right(current_position), ["R", "F"]))
            stack_moves.append((self.move_forward(current_position), ["F"]))
        if len(path) > 0:
            # a path is found. Remove the command None though (used only for internal behaviour)
            path.pop(0)
            return path
        else:
            return None

    def escape(self):
        return super().escape(escape_func=self.iterative_escape)
