import random

def initialize_grid():
    grid = [[0] * 4 for _ in range(4)]
    add_random_tile(grid)
    add_random_tile(grid)
    return grid

def add_random_tile(grid):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = 2

# Move non-empty cells to one direction
def compress(grid):
    new_grid = [[0] * 4 for _ in range(4)]
    for i in range(4):
        position = 0
        for j in range(4):
            if grid[i][j] != 0:
                new_grid[i][position] = grid[i][j]
                position += 1
    return new_grid

def merge(grid):
    for i in range(4):
        for j in range(3):
            if grid[i][j] == grid[i][j + 1] and grid[i][j] != 0:
                grid[i][j] = grid[i][j] + grid[i][j + 1]
                grid[i][j + 1] = 0
    return grid

# Retate the grid clockwise
def rotate_90(grid):
    return [list(row) for row in zip(*grid[::-1])]

# Move functions for up, down, left, right
def move_left(grid):
    compressed_grid = compress(grid)
    merged_grid = merge(compressed_grid)
    final_grid = compress(merged_grid)
    return final_grid

def move_right(grid):
    rotated = rotate_90(rotate_90(grid)) # rotate 180 degrees
    new_grid = move_left(rotated) # rotate 180 and move left = move right
    return rotate_90(rotate_90(new_grid)) # rotate back to original

def move_down(grid):
    rotated = rotate_90(grid) # rotate 90 degrees
    new_grid = move_left(rotated) # rotate 90 + move left = move down
    return rotate_90(rotate_90(rotate_90(new_grid))) # rotate back to original

def move_up(grid):
    rotated = rotate_90(rotate_90(rotate_90(grid))) # rotate 90 degrees counter-clockwise
    new_grid = move_left(rotated) # rotate 90 degrees counter-clockwise + move left = move up
    return rotate_90(new_grid) # rotate back to original

def check_win(grid):
    for row in grid:
        for cell in row:
            if cell == 2048:
                return True
    return False

def check_lose(grid):
    # Check for any empty cell
    for row in grid:
        for cell in row:
            if cell == 0:
                return False
    
    # Check for possible merges in each row and column
    for i in range(4):
        for j in range(3):
            # Check adjacent cells in the row
            if grid[i][j] == grid[i][j + 1]:
                return False
            # Check adjacent cells in the column
            if grid[j][i] == grid[j + 1][i]:
                return False
    return True