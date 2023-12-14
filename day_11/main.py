galaxy_map = []

def process_input(f):
    galaxy = []
    for line in f:
        galaxy.append(list(line.strip()))
    return galaxy

def dupe_column(lst, col, offset):
    for row in lst:
        row.insert(row.index(row[col]) + offset, '.')
    return lst

def expand_galaxy(galaxy):
    expansions = [[], []]
    x_length, y_length = len(galaxy[0]), 0
    for y, row in enumerate(galaxy):
        if not '#' in row:
            expansions[1].append(y)
        for column, x in enumerate(row):
            if x == '.':
                expansions[0].append(column)
        y_length += 1
    
    yexp_count = 0
    for y in expansions[1]:
        galaxy.insert(y + yexp_count, list('.' * x_length))
        yexp_count += 1
    
    return galaxy

with open("input.txt") as f:
    galaxy_map = process_input(f)
    galaxy_map = expand_galaxy(galaxy_map)
    print(*galaxy_map, sep='\n')
