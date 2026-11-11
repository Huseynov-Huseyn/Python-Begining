# ==========================================
# Exercise 18: Tic-Tac-Toe Game
# ==========================================
#
# Overview:
# Build a 2-player or Player vs. Computer Tic-Tac-Toe game in the terminal.
#
# Requirements & Rules:
# 1. Board Representation:
#    - Create a 3x3 grid (using a 2D list or a 9-element list) initialized with empty spaces.
# 2. Display Board:
#    - Create a function (e.g., `print_board`) to display the current grid nicely in the console.
# 3. Player Moves:
#    - Prompt players ('X' and 'O') to enter their move (e.g., positions 1-9 or row/column index).
#    - Validate input: ensure the chosen position is within range and not already occupied.
# 4. Check Winner & Draw:
#    - Check all 8 winning conditions (3 rows, 3 columns, 2 diagonals).
#    - Check for a tie/draw if all spots are filled with no winner.
# 5. Game Loop:
#    - Alternate turns between Player 1 ('X') and Player 2 / Computer ('O').
#    - Continue until someone wins or the game ends in a tie.
#
# Suggested Functions:
# - print_board()
# - player_move()
# - computer_move()   # (Optional: for Player vs Computer mode)
# - check_winner()
# - check_tie()
# - main()
#
# Write your code below:
import random

board = [["*", "*", "*"],
         ["*", "*", "*"],
         ["*", "*", "*"]]


def print_board():
    for x in range(3):
        for y in range(3):
            if y == 2:
                print(board[x][y])
            else:
                print(board[x][y], end=" | ")
        print("----------")


def player_move():
    while True:
        row = input("Please enter a row(1-3): ")
        column = input("Please enter a column(1-3): ")
        if not (row.isdigit() and column.isdigit()):
            print("Invalid input!")
            continue
        row = int(row) - 1
        column = int(column) - 1
        if not (0 <= row < 3 and 0 <= column < 3):
            print("Invalid input!")
            continue
        if board[row][column] != "*":
            print("This place is occupied!")
            continue
        board[row][column] = "X"
        return


def computer_move():
    while True:
        row = random.randint(0, 2)
        column = random.randint(0, 2)
        if board[row][column] != "*":
            continue
        else:
            board[row][column] = "O"
            return


def check_winner():
    winning_lines = [
        # 3 row
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # 3 column
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # 2 diagonal
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    for line in winning_lines:
        if line[0] == line[1] == line[2] != "*":
            return line[0]
    if not any("*" in row for row in board):
        return "Tie"
    else:
        return None


def game_over():
    condition = check_winner()
    if condition == "X":
        print("Player win!")
        print_board()
        return True
    elif condition == "O":
        print("Computer win!")
        print_board()
        return True
    elif condition == "Tie":
        print("Tie!")
        print_board()
        return True
    else:
        return False


def main():
    print("=========================")
    print("Welcome Tic Tac Toe Game!")
    print("=========================")

    while True:
        print_board()
        player_move()
        if game_over():
            break
        computer_move()
        if game_over():
            break


if __name__ == "__main__":
    main()
