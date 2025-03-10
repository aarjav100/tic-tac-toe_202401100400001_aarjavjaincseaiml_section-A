import math

# Initialize the board
board = [' ' for _ in range(9)]  # 3x3 Tic-Tac-Toe grid



# Check if a player has won
def check_win(board, player):
    win_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
                     (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
                     (0, 4, 8), (2, 4, 6)]            # Diagonals
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_positions)



# Check if the board is full
def is_full(board):
    return ' ' not in board


# Minimax Algorithm
def minimax(board, depth, is_maximizing):
    if check_win(board, 'X'):
        return 10 - depth
    if check_win(board, 'O'):
        return depth - 10
    if is_full(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = max(best, minimax(board, depth + 1, False))
                board[i] = ' '
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = min(best, minimax(board, depth + 1, True))
                board[i] = ' '
        return best




# Find the best move for the AI (X)
def find_best_move(board):
    best_value = -math.inf
    best_move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            move_value = minimax(board, 0, False)
            board[i] = ' '
            if move_value > best_value:
                best_value = move_value
                best_move = i

    return best_move




# Display the board
def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])
        if i < 6:
            print('--+---+--')
    print()




# Example of running the solver
print("Initial Board:")
print_board(board)

move = find_best_move(board)
print(f"AI's best move is at index {move}")




# Make the AI move
board[move] = 'X'
print("Board after AI move:")
print_board(board)
