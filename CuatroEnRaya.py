class CuatroEnRaya:

    def __init__(self, rows, columns):
        """
        Inicializa el estado de la clase.

        Parametros posicionales:
        filas --- int cantidad de filas dle tablero
        columnas --- int cantidad de columnas del tablero
        """

        self._rows = rows
        self._columns = columns
        self._board = self.create_board()
        self._turn = None

    def create_board(self):
        """
        Crea el tablero de juego
        :param rows: int --- representa numero de filas
        :param columns: int --- representa numero de columnas
        """
        # Lista inicial vacia
        board = [None] * self._rows

        for f in range(self._rows):
            board[f] = ['.'] * self._columns

        return board

    def show_board(self):
        """
        Muestra el tablero por pantalla.
        :param board: list --- tablero a mostrar
        """

        # Sacamos por pantalla la cabecera de columnas
        for num in range(self._columns):
            print(num, end='  ')

        # Sacamos por pantalla el tablero
        for row in self._board:
            print("")  # hace el cambio de linea de cada fila
            for box in row:
                print(box, end="  ")

    def insert_tab(self, column, color):
        """
        Esta funcion introduce una ficha en el tablero.
        :param column: int --- columna del tablero donde se va a ingresar
        :param color: str --- simbolo que se ingresara
        """
        if column >= self._columns or column < 0:
            print("ERROR: Numero de columna fuera de rango.")
            return
        elif self._board[0][column] != '.':
            print("ERROR: La columna esta llena de fichas")
            return
        else:
            for row in range(self._rows - 1, -1, -1):
                if self._board[row][column] == '.':
                    self._board[row][column] = color
                    return

    def _check_rows(self, color):
        """
        Esta funcion revisa si hay 4 objetos iguales en filas
        :param board: list --- tablero a revisar
        :param color: str --- objeto que esta repetido 4 veces
        """

        # Recorremos las filas en busca de 4 en raya
        for r in range(self._rows):
            for c in range(self._columns - 3):
                if self._board[r][c] == color and self._board[r][c + 1] == color and self._board[r][c + 2] == color and self._board[r][c + 3] == color:
                    return True

    def _check_columns(self, color):
        """
        Esta funcion revisa si hay 4 objetos iguales en columnas
        :param color: str --- objeto que esta repetido 4 veces
        """

        # Recorremos las filas en busca de 4 en raya
        for c in range(self._columns):
            for r in range(self._rows - 3):
                if self._board[r][c] == color and self._board[r + 1][c] == color and self._board[r + 2][c] == color and self._board[r + 3][c] == color:
                    return True

    def _check_right_diagonal(self, color):
        """
        Revisa si hay 4 objetos iguales en la diagonal derecha
        :param color: str --- objeto que esta repetido 4 veces
        """

        # Recorremos las filas en busca de 4 en raya
        for c in range(self._columns - 3):
            for r in range(self._rows - 1, 2, -1):
                if self._board[r][c] == color and self._board[r - 1][c + 1] == color and self._board[r - 2][c + 2] == color and self._board[r - 3][c + 3] == color:
                    return True

    def _check_left_diagonal(self, color):
        """
        Revisa si hay 4 objetos iguales en la diagonal izquierda
        :param color: str --- objeto que esta repetido 4 veces
        """

        # Recorremos las filas en busca de 4 en raya
        for c in range(self._columns - 1, 2, -1):
            for r in range(self._rows - 1, 2, -1):
                if self._board[r][c] == color and self._board[r - 1][c - 1] == color and self._board[r - 2][c - 2] == color and self._board[r - 3][c - 3] == color:
                    return True

    def check_winner(self, color):
        """
        Comprueba si se ha producido un cuatro en raya.
        Agrupa los metodos anteriores.
        :param color: str --- objeto que esta repetido 4 veces
        """
        return self._check_rows(color) or self._check_columns(color) or self._check_right_diagonal(color) or self._check_left_diagonal(color)

    def play(self, player1 = 'X', player2 = 'O'):
        self._turn = player2
        while True:
            self._turn = player1 if self._turn == player2 else player2
            self.show_board()
            column = int(input("Turno del jugador {}:".format(self._turn)))
            self.insert_tab(column, self._turn)
            if self.check_winner(self._turn):
                print("\n\nHa ganado el jugador {}!!\n\n".format(self._turn))
                self.show_board()
                break

