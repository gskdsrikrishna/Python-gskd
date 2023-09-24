#Crossword Puzzle Generater
import random
from typing import List, Tuple

def generate_crossword(word_list: List[str]) -> List[List[str]]:
    # Sort word list by length in descending order
    word_list.sort(key=lambda word: len(word), reverse=True)

    # Initialize an empty grid for the crossword puzzle
    grid = [[' ' for _ in range(15)] for _ in range(15)]

    # Place the first word horizontally at a random position
    start_x = random.randint(0, 15 - len(word_list[0]))
    start_y = random.randint(0, 14)
    place_word(grid, word_list[0], start_x, start_y, 1)

    # Place the remaining words vertically or horizontally
    for word in word_list[1:]:
        placed = False
        while not placed:
            # Randomly choose whether to place the word vertically or horizontally
            direction = random.choice(['vertical', 'horizontal'])
            if direction == 'vertical':
                start_x = random.randint(0, 14)
                start_y = random.randint(0, 15 - len(word))
                if check_vertical_placement(grid, word, start_x, start_y):
                    place_word(grid, word, start_x, start_y, -1)
                    placed = True
            else:
                start_x = random.randint(0, 15 - len(word))
                start_y = random.randint(0, 14)
                if check_horizontal_placement(grid, word, start_x, start_y):
                    place_word(grid, word, start_x, start_y, 1)
                    placed = True

    return grid

def place_word(grid: List[List[str]], word: str, start_x: int, start_y: int, step: int) -> None:
    for i in range(len(word)):
        grid[start_y + i * step][start_x] = word[i]

def check_vertical_placement(grid: List[List[str]], word: str, start_x: int, start_y: int) -> bool:
    if start_y + len(word) > 15:
        return False
    for i in range(len(word)):
        if grid[start_y + i][start_x] != ' ' and grid[start_y + i][start_x] != word[i]:
            return False
    return True

def check_horizontal_placement(grid: List[List[str]], word: str, start_x: int, start_y: int) -> bool:
    if start_x + len(word) > 15:
        return False
    for i in range(len(word)):
        if grid[start_y][start_x + i] != ' ' and grid[start_y][start_x + i] != word[i]:
            return False
    return True

def print_grid(grid: List[List[str]]) -> None:
    for row in grid:
        print(' '.join(row))

# Example usage:
word_list = ['python', 'algorithm', 'programming', 'code', 'crossword', 'puzzle']
crossword = generate_crossword(word_list)
print_grid(crossword)