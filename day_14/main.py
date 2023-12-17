import numpy as np

DIRECTIONS = ( (0, -1), (-1, 0), (0, 1), (1, 0) )

rock_grid = None
grid_width = 0
grid_height = 0

cycles = 1000000000

def process_input(f):
    rock_grid = np.array([])
    width = 0
    height = 0
    
    for y, line in enumerate(f):
        row = np.array(list(line.strip()))
        width = len(row)
        height += 1
        
        try:
            rock_grid = np.vstack((rock_grid, row))
        except ValueError:
            rock_grid = row
    
    return rock_grid, width, height

def move_rocks(grid, direction):
    new_grid = grid
    moved = 0
    
    for y, row in enumerate(new_grid):
        for x in np.where(row == 'O')[0]:
            try:
                new_x, new_y = x + direction[0], y + direction[1]
                if new_grid[new_y][new_x] == '.':
                    if new_y < 0 or new_y > grid_height or new_x < 0 or new_x > grid_width:
                        continue
                    new_grid[y][x] = '.'
                    
                    new_grid[new_y][new_x] = 'O'
                    moved += 1
            except IndexError:
                continue
    return new_grid, moved

def calculate_load(rock_grid):
    total_load = 0
    for y, row in enumerate(rock_grid):
        for x in np.where(row == 'O')[0]:
            load = grid_height - y
            total_load += load
            #print(f"Rock at {x, y} has a load of {load}.")
    return total_load

with open("input.txt") as f:
    rock_grid, w, h = process_input(f)
    grid_width = w
    grid_height = h

cycle_frequency = {}

while cycles != 0:
    for i in range(4):
        direction = DIRECTIONS[i]
        amount_moved = None
        while amount_moved != 0:
            rock_grid, moved = move_rocks(rock_grid, direction)
            amount_moved = moved
        #print(rock_grid, '\n')
        #print("\n----------------------------------------\n")
    cycles -= 1
    total_load = calculate_load(rock_grid)
    cycle_frequency[total_load] = cycle_frequency.get(total_load, 0) + 1

    print(f"CYCLES_LEFT = {cycles}, with a load of {total_load}. The frequencies are: {cycle_frequency}")

print("\n----------------------------------------\n")
print(f"All rocks moved far north, the grid at a width of {grid_width} and height of {grid_height}.")
print(f"The total load is {total_load}.")
