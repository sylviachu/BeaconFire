import copy
from functions import (
    initialize_grid, add_random_tile, move_left, move_right, move_up, move_down,
    check_win, check_lose
)

def display_grid(grid):
    for row in grid:
        print("+----" * 4 + "+")
        print("|" + "|".join(f"{num:^4}" if num != 0 else "    " for num in row) + "|")
    print("+----" * 4 + "+")

def main():
    grid = initialize_grid()
    display_grid(grid)
    
    while True:
        move = input("Moving direction: (w=up, s=down, a=left, d=right, q=quit): ").lower()
        if move not in "wsadqr":
            print("Invalid input. Please enter w, s, a, d, or q.")
            continue
        
        if move == 'q':
            print("Game over.")
            break
            
        if move == 'r':
            # Restart the game
            print("Game Restarted!")
            grid = initialize_grid()
            display_grid(grid)
            continue
            
        grid_before_move = copy.deepcopy(grid)
        
        # moving direction
        if move == 'w':
            grid = move_up(grid)
        elif move == 's':
            grid = move_down(grid)
        elif move == 'a':
            grid = move_left(grid)
        elif move == 'd':
            grid = move_right(grid)
        
        if grid != grid_before_move: # add new tile only when the old tiles have moved
            add_random_tile(grid)

        display_grid(grid)

        if check_win(grid):
            print("You Win!")
            break
        if check_lose(grid):
            print("No more moves left! Game over.")
            break

if __name__ == "__main__":
    main()