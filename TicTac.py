from tkinter import messagebox
import tkinter as tk
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

# Función para generar el árbol de búsqueda


def generate_tree(board, player):
    possible_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                future_board = copy.deepcopy(board)
                future_board[i][j] = player
                possible_moves.append(
                    (i, j, evaluate_move(future_board, 3 - player)))

    return possible_moves

# Función para evaluar una jugada en el árbol


def evaluate_move(board, player):
    if check_win(board, player):
        return WIN_SCORE
    elif check_win(board, 3 - player):
        return LOSE_SCORE
    else:
        future_moves = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    future_board = copy.deepcopy(board)
                    future_board[i][j] = player
                    future_score = evaluate_move(future_board, 3 - player)
                    future_moves.append(future_score)

# Función para imprimir el tablero con "X" y "O"


def print_board(board):
    for row in board:
        print(" | ".join(
            ["X" if cell == X else "O" if cell == O else " " for cell in row]))
        print("-" * 9)

# Función principal para mostrar las evaluaciones


def lshow_evaluations():
    initial_board = [[EMPTY, EMPTY, EMPTY],
                     [EMPTY, EMPTY, EMPTY],
                     [EMPTY, EMPTY, EMPTY]]
    print_board(f"Tablero inicial: {initial_board}")
    print_board(initial_board)

    player = X

    # Evaluar si el jugador gana
    if check_win(initial_board, player):
        winner_score = WIN_SCORE
        print(f"Puntuación: {winner_score} puntos: Ganaste\n")
        return
    elif check_win(initial_board, player):
        winner_score = LOSE_SCORE
        print(f"Puntuación: {winner_score} puntos: Perdiste\n")
        return
    else:
        winner_score = NEUTRAL_SCORE
        print("-----------------------------------Posibles Movimientos-----------------------------------")
        evaluate_and_print(initial_board, player, winner_score)


def evaluate_and_print(board, player, winner_score):
    possible_moves = generate_tree(board, player)
    for move in possible_moves:
        i, j, score = move
        print(f"\nEvaluación para colocar {player} en ({i}, {j}):")

        future_board = copy.deepcopy(board)
        future_board[i][j] = player
        print_board(future_board)

        # Evaluar si el jugador gana en una jugada futura
        if check_win(future_board, player) and player == 1:
            winner_score = FUTURE_WIN_SCORE
            print(
                f"Puntuación: {winner_score} puntos: Ganaste en esta futura jugada\n")
            print(
                "----------------------------------------------------------------------")
        elif check_win(future_board, player) and player == 2:
            winner_score = FUTURE_LOSE_SCORE
            print(f"Puntuación: {winner_score} puntos: Perdiste en una futura jugada\n")
            print(
             "----------------------------------------------------------------------")
        else: 
            evaluate_and_print(future_board, 3 - player, winner_score)
            
            if move == possible_moves[-1] and winner_score == NEUTRAL_SCORE:
                print(f"Puntuación: {winner_score} puntos: Empate\n")
                print(
                    "----------------------------------------------------------------------")


class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = X
        self.board = [[EMPTY, EMPTY, EMPTY],
                      [EMPTY, EMPTY, EMPTY],
                      [EMPTY, EMPTY, EMPTY]]

        self.buttons = [[None]*3 for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(  # type: ignore
                    root, text="", font=("Helvetica", 16), height=2, width=5,
                    command=lambda row=i, col=j: self.on_button_click(row, col)
                )
                self.buttons[i][j].grid(row=i, column=j)  # type: ignore

        self.show_solution_button = tk.Button(
            root, text="Show Solution", font=("Helvetica", 12),
            command=self.show_solution
        )
        self.show_solution_button.grid(row=3, columnspan=3)

        self.reset_game()

    def on_button_click(self, row, col):
        if self.board[row][col] == EMPTY:
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(
                text="X" if self.current_player == X else "O"
            )

            if check_win(self.board, self.current_player):
                messagebox.showinfo(
                    "Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif all(cell != EMPTY for row in self.board for cell in row):
                messagebox.showinfo(
                    "Game Over", "It's a tie! Puntuación: 0 puntos:")
                self.reset_game()
            else:
                self.current_player = 3 - self.current_player  # Switch player

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = EMPTY
                self.buttons[i][j].config(text="")  # type: ignore
        self.current_player = X

    def show_solution(self):
        winner_score = NEUTRAL_SCORE
        evaluate_and_print(self.board, self.current_player, winner_score)


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
