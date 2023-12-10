histories = []
extrapolated_total = 0

part = 2

def create_sequence(hist: list):
    sequence = []
    if part == 2:
        hist.reverse()
    sequence.append(hist)


    layer = 0

    print(*hist, sep="   ")
    while sequence[-1].count(0) != len(sequence[-1]):
        new_layer = []
        for index, val in enumerate(sequence[layer]):
            try:
                new_val = sequence[layer][index + 1] - val
                new_layer.append(new_val)
            except IndexError:
                break
        
        sequence.append(new_layer)

        print("  " * (layer + 1), end='')
        print(*new_layer, sep="   ")
        layer += 1

    for i, v in reversed(list(enumerate(sequence))):
        if i == len(sequence) - 1:
            sequence[i].append(0)
        elif i == 0:
            break
        sequence[i - 1].append(v[-1] + sequence[i - 1][-1])

    print(f"Sequence: {sequence}\n")
    return sequence


with open("input.txt") as f:
    for line in f:
        hist = [int(x) for x in line.strip().split(' ')]
        sequence = create_sequence(hist)
        histories.append(sequence)

for history in histories:
    extrapolated_total += history[0][-1]

print("\n-------------------------------\n")
print(f"Extrapolated total: {extrapolated_total}")
