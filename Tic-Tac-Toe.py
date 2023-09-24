#Tic-Tac-Toe
import random

def draw_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], end=" | ")
        print("\n-------------")

def is_winner(board, player):
    # Check rows
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True

    # Check columns
    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

def get_player_move(board):
    while True:
        move = input("Enter your move (row [1-3] and column [1-3]): ")
        move = move.split()
        if len(move) != 2:
            print("Invalid input. Please try again.")
            continue
        row, col = move
        if not (row.isdigit() and col.isdigit()):
            print("Invalid input. Please try again.")
            continue
        row = int(row) - 1
        col = int(col) - 1
        if not (0 <= row < 3 and 0 <= col < 3):
            print("Invalid input. Please try again.")
            continue
        if board[row][col] != " ":
            print("Cell already occupied. Please try again.")
            continue
        return row, col

def get_computer_move(board):
    # Check for winning moves
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                if is_winner(board, "O"):
                    return i, j
                else:
                    board[i][j] = " "

    # Check for blocking moves
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                if is_winner(board, "X"):
                    return i, j
                else:
                    board[i][j] = " "

    # Choose a random move
    available_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                available_moves.append((i, j))
    return random.choice(available_moves)

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    draw_board(board)

    while True:
        if player == "X":
            row, col = get_player_move(board)
            board[row][col] = player
        else:
            print("Computer's turn:")
            row, col = get_computer_move(board)
            board[row][col] = player

        draw_board(board)

        if is_winner(board, player):
            if player == "X":
                print("Congratulations! You won!")
            else:
                print("Computer wins! Better luck next time.")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"

play_game()