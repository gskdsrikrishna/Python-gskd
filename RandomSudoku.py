import random
import numpy as np

def generate_random_sudoku(difficulty):
    # Initialize an empty Sudoku grid
    grid = np.zeros((9, 9), dtype=int)

    # Fill the diagonal 3x3 grids with random numbers
    for i in range(0, 9, 3):
        nums = random.sample(range(1, 10), 3)
        for j in range(3):
            grid[i + j, i + j] = nums[j]

    # Solve the Sudoku grid
    solve_sudoku(grid)

    # Remove numbers from the solved Sudoku grid to create the puzzle
    num_cells_to_remove = 81 - difficulty
    while num_cells_to_remove > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if grid[row, col] != 0:
            grid[row, col] = 0
            num_cells_to_remove -= 1

    return grid

def solve_sudoku(grid):
    # Solve the Sudoku grid using backtracking
    solve_sudoku_helper(grid, 0, 0)

def solve_sudoku_helper(grid, row, col):
    # Base case: If the entire grid is filled, return True
    if row == 9:
        return True

    # Calculate the next row and column indices
    next_row, next_col = calculate_next_indices(row, col)

    # If the current cell is already filled, move to the next cell
    if grid[row, col] != 0:
        return solve_sudoku_helper(grid, next_row, next_col)

    # Try different numbers from 1 to 9
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row, col] = num
            if solve_sudoku_helper(grid, next_row, next_col):
                return True
            grid[row, col] = 0

    # If no number from 1 to 9 works, backtrack
    return False

def calculate_next_indices(row, col):
    # Calculate the next row and column indices
    if col == 8:
        return row + 1, 0
    else:
        return row, col + 1

def is_valid_move(grid, row, col, num):
    # Check if the current number is valid in the given position
    return (
        is_valid_in_row(grid, row, num) and
        is_valid_in_column(grid, col, num) and
        is_valid_in_box(grid, row - row % 3, col - col % 3, num)
    )

def is_valid_in_row(grid, row, num):
    # Check if the current number is valid in the given row
    return num not in grid[row, :]

def is_valid_in_column(grid, col, num):
    # Check if the current number is valid in the given column
    return num not in grid[:, col]

def is_valid_in_box(grid, box_start_row, box_start_col, num):
    # Check if the current number is valid in the given 3x3 box
    return num not in grid[box_start_row : box_start_row + 3, box_start_col : box_start_col + 3]

# Example usage:
difficulty_level = 50  # Number of cells to remove to make it a puzzle
random_sudoku = generate_random_sudoku(difficulty_level)
print(random_sudoku)
