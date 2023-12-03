import math, string

SYMBOLS = string.punctuation.replace('.', '')
NUMBERS = string.digits
DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (-1,1), (-1,-1), (1,-1)]

schematic = []

adj_sums = 0
total_gear_ratios = 0

def process_input(str):
    schem = []
    for c in str.strip():
        schem.append(c)
    
    schem_line = []
    prev_digits = ""
    for c in schem:
        if c in NUMBERS:
            prev_digits += c
        else:
            if prev_digits != "":
                schem_line.extend([prev_digits] * len(prev_digits))
            else:
                prev_digits = " "
            schem_line.append(c)
            prev_digits = ""
    else:
        if prev_digits != "":
            schem_line.extend([prev_digits] * len(prev_digits))

    return schem_line

def check_adjacents(x, y):
    adjacent = False
    for direction in DIRECTIONS:
        try:
            if schematic[y + direction[1]][x + direction[0]] in SYMBOLS:
                adjacent = True
                break
        except IndexError:
            pass
            #print("Invalid location.")
    
    return adjacent

def check_gear_adjacents(x, y):
    adjacents = []

    for direction in DIRECTIONS:
        try:
            location_val = schematic[y + direction[1]][x + direction[0]]
            if location_val.isnumeric():
                if not (int(location_val), y) in adjacents:
                    adjacents.append((int(location_val), y))
        except IndexError:
            pass
            #print("Invalid location.")

    return [x[0] for x in adjacents]

with open("input.txt") as f:
    for line in f:
        schematic.append(process_input(line))

adjs = 0
for y, row in enumerate(schematic):
    adjacents = []
    prevadj = None
    print(f"\n{row} LEN = {len(row)}")
    for x, v in enumerate(row):
        if v.isnumeric():
            adjacent = check_adjacents(x, y)
            if adjacent and v != prevadj:
                adjacents.append(int(v))
                prevadj = v
        elif v == '*':
            gear_adjacents = check_gear_adjacents(x, y)
            if len(gear_adjacents) == 2:
                total_gear_ratios += math.prod(gear_adjacents)
                print(f"* adjacents: {gear_adjacents}")
    
    adj_sums += sum(adjacents)
    adjs += len(adjacents)
    print(f"{adjacents} are adjacent to a symbol.")

print("\n-----------------------------------------------")
print(f"There were {adjs} numbers adjacent to a symbol.")
print(f"The adjacant sum is: {adj_sums}, with the total gear ratios being {total_gear_ratios}")
