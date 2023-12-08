directions = []
map_lst = {}

def process_input(line): 
    split = line.strip().split(" = ")
    node = split[0]
    dirs = split[1].replace('(', '').replace(')', '').split(", ")

    return node, tuple(dirs)

def get_turns(): 
    turns = 0 
    currently_at = "AAA"
    while currently_at != "ZZZ":
        direction = directions[turns % len(directions)]
        currently_at = map_lst[currently_at][direction]
        turns += 1

    return turns

with open("input.txt") as f:
    directions = list(f.readline().strip())
    directions = list(map(lambda x: 1 if x == 'R' else 0, directions))
    f.readline()

    for line in f:
        node, dirs = process_input(line)
        map_lst[node] = dirs

turns = get_turns()

print(directions, map_lst)
print(f"\nStarting from 'AAA', it took {turns} turns to reach 'ZZZ'")
