def hash_algo(seq) -> int:
    out = 0
    for c in seq:
        out = ((out + ord(c)) * 17) % 256
    
    #print(f"{seq}: {out}")
    return out

with open("input.txt") as f:
    sequence = f.read().strip().split(',')

total = sum([hash_algo(x) for x in sequence])


boxes = {} # box_num: [[rn 1], ...] 

for seq in sequence:
    operation = '=' if '=' in seq else '-'
    label, val = seq.split(operation)
    print(seq)

    box_num = hash_algo(label)
    if not box_num in boxes: boxes[box_num] = []
    
    print(f"Lens {label, val} with num {box_num}, operation ({operation})")

    if operation == '=':
        new_lens = (label, val)
        replaced = False

        for i, lens in enumerate(boxes[box_num]):
            if lens[0] == label:
                boxes[box_num][i] = new_lens
                replaced = True
                break
        if replaced: continue

        boxes[box_num].append(new_lens)
    else:
        for i, lens in enumerate(boxes[box_num]):
            if lens[0] == label:
                boxes[box_num].pop(i)
                break

lens_total = 0
for box_num, seq in boxes.items():
    for slot, lens in enumerate(seq):
        lens_total += (box_num + 1) * (slot + 1) * int(lens[1])

print(boxes)

print(f"\nHASH algorithm total: {total}")
print(f"Lens total is {lens_total}")
