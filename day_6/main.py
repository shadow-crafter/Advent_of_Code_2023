import math

times = []
distances = []

def process_input(line):
    split1 = line.strip().split(' ')
    converted = list(map(lambda x: int(x) if x.isnumeric() else None, split1))
    filtered = [x for x in converted if x != None]

    return filtered

def get_wins():
    win_methods = []
    for i, time in enumerate(times):
        wins_possible = 0
        for ms_held in range(time):
            distance_traveled = ms_held * (time - ms_held)
            if distance_traveled > distances[i]:
                wins_possible += 1
        win_methods.append(wins_possible)

    return win_methods

with open("input.txt") as f:
    times = process_input(f.readline())
    distances = process_input(f.readline())

wins_possible = get_wins()

print(f"Times: {times} \nDistances: {distances} \nWin List: {wins_possible}")
print(f"\nAnswer: {math.prod(wins_possible)}")
