#Sudoku Solver
def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True

    row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, num, row, col):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False

def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None

def is_valid(board, num, row, col):
    # Check if the number is already in the same row
    if num in board[row]:
        return False

    # Check if the number is already in the same column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check if the number is already in the same 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def print_board(board):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - -")
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("|", end=" ")
            print(board[row][col], end=" ")
        print()

def sudoku_solver():
    print("Enter the Sudoku puzzle (use '0' for empty cells):")
    board = []
    for _ in range(9):
        row = list(map(int, input().split()))
        board.append(row)

    if solve_sudoku(board):
        print("\nSudoku solved:")
        print_board(board)
    else:
        print("No solution exists for the given Sudoku puzzle.")

sudoku_solver()