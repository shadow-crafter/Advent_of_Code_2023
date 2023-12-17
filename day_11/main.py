with open("test.txt") as f:
    grid = f.read().splitlines()

rows = [i for i, row in enumerate(grid) if row == ('.' * len(grid[0]))]
columns = [i for i, column in enumerate(zip(*grid)) if all(c == '.' for c in column)]

galaxy_locations = [(x, y) for y, row in enumerate(grid) for x, column in enumerate(row) if column == '#']

sums = []
for i1, (x1, y1) in enumerate(galaxy_locations):
    for i2, (x2, y2) in enumerate(galaxy_locations):
        if i1 == i2: continue

        dist = abs(x1 - x2) + abs(y1 - y2)
        print(dist)

print(f"{grid} \nRows: {rows} \nCols: {columns}")
