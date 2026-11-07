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
#    - Ask if the players want to play again.
#
# Suggested Functions:
# - print_board(board)
# - player_move(board, player)
# - computer_move(board)   # (Optional: for Player vs Computer mode)
# - check_winner(board)
# - check_tie(board)
# - main()
#
# Write your code below:
