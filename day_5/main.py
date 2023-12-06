almanac = []

def process_input(file):
    seeds = []
    for line in file:
        line = line.strip()
        if "seeds:" in line:
            seeds = line.replace("seeds: ", '').split(' ')
            seeds = [int(x) for x in seeds]
        elif "-to-" in line:
            pass
        else:
            pass
    
    print(seeds)

with open("input.txt") as f:
    process_input(f)
