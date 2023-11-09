import copy

# Constantes para las puntuaciones
WIN_SCORE = 10
FUTURE_WIN_SCORE = 5
NEUTRAL_SCORE = 0
FUTURE_LOSE_SCORE = -5
LOSE_SCORE = -10

# Representación del tablero 3x3 como una lista de listas
EMPTY = 0
X = 1
O = 2

# Función para imprimir el tablero
def print_board(board):
    for row in board:
        print(" | ".join(["X" if cell == X else "O" if cell == O else " " for cell in row]))
        print("-" * 9)

# Función para verificar si un jugador ha ganado
def check_win(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Función para evaluar una jugada en el árbol
def evaluate_move(board, player):
    if check_win(board, player):
        return WIN_SCORE
    elif check_win(board, 3 - player):
        return LOSE_SCORE
    elif all(cell != EMPTY for row in board for cell in row):
        return NEUTRAL_SCORE
    else:
        future_moves = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    future_board = copy.deepcopy(board)
                    future_board[i][j] = player
                    future_moves.append((i, j, evaluate_move(future_board, 3 - player)))

        best_future_score = min(future_moves, key=lambda x: x[2])[2] if future_moves else NEUTRAL_SCORE

        if player == X:
            if best_future_score == WIN_SCORE:
                return WIN_SCORE
            elif best_future_score == LOSE_SCORE:
                return LOSE_SCORE
            elif best_future_score == FUTURE_WIN_SCORE:
                return FUTURE_WIN_SCORE
            elif best_future_score == FUTURE_LOSE_SCORE:
                return FUTURE_LOSE_SCORE
            else:
                return NEUTRAL_SCORE
        else:
            if best_future_score == WIN_SCORE:
                return LOSE_SCORE
            elif best_future_score == LOSE_SCORE:
                return WIN_SCORE
            elif best_future_score == FUTURE_WIN_SCORE:
                return FUTURE_LOSE_SCORE
            elif best_future_score == FUTURE_LOSE_SCORE:
                return FUTURE_WIN_SCORE
            else:
                return NEUTRAL_SCORE

# Función para generar el árbol de búsqueda
def generate_tree(board, player, depth):
    if depth == 0:
        return NEUTRAL_SCORE
    possible_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                future_board = copy.deepcopy(board)
                future_board[i][j] = player
                possible_moves.append((i, j, generate_tree(future_board, 3 - player, depth - 1)))
    if player == X:
        return max(possible_moves, key=lambda x: x[2])
    else:
        return min(possible_moves, key=lambda x: x[2])

# Función principal para el juego
def play_tictactoe():
    board = [[EMPTY] * 3 for _ in range(3)]
    current_player = X
    max_moves = 9  # Número máximo de movimientos permitidos en un juego de Tic-Tac-Toe

    for move_count in range(max_moves):
        print_board(board)
        available_moves = get_available_moves(board)
        if not available_moves:
            print("¡Empate!")
            break

        print(f'Turno de Jugador {current_player}:')
        if current_player == X:
            print("Movimientos disponibles:", available_moves)
            row, col = map(int, input("Ingrese la fila y columna (0-8) separadas por espacio: ").split())
        else:
            print("Movimientos disponibles:", available_moves)
            row, col = map(int, input("Ingrese la fila y columna (0-8) separadas por espacio: ").split())

        if (row, col) not in available_moves:
            print("Movimiento no válido. Intente de nuevo.")
            continue

        board[row][col] = current_player
        score = evaluate_move(board, current_player)
        print(f"Puntuación del movimiento: {score}")

        if check_win(board, current_player):
            print_board(board)
            print(f"¡Jugador {current_player} gana!")
            break
        elif move_count == max_moves - 1:
            print("¡Empate!")

        current_player = X if current_player == O else O

def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.append((i, j))
    return moves

if __name__ == "__main__":
    play_tictactoe()
