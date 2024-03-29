import math

races = [[], []]
real_race = [[], []]

def process_input(line):
    split1 = line.strip().split(' ')
    converted = list(map(lambda x: int(x) if x.isnumeric() else None, split1))
    filtered_race = [x for x in converted if x != None]

    split2 = line.strip().split(':')[1].replace(' ', '')
    combined = [int(''.join(split2))]

    return filtered_race, combined

def get_wins(race):
    win_methods = []
    for i, time in enumerate(race[0]):
        wins_possible = 0
        for ms_held in range(time):
            distance_traveled = ms_held * (time - ms_held)
            if distance_traveled > race[1][i]:
                wins_possible += 1
        win_methods.append(wins_possible)

    return win_methods

with open("input.txt") as f:
    races[0], real_race[0] = process_input(f.readline())
    races[1], real_race[1] = process_input(f.readline())

wins_possible = math.prod(get_wins(races))
real_wins_possible = math.prod(get_wins(real_race))

print(f"Times: {races[0]} \nDistances: {races[1]} \nWin List: {wins_possible}")
print(f"\nAnswer: {wins_possible}, Real: {real_wins_possible}")
