### PROCESS INPUT DATA
with open("input.txt", encoding="utf-8") as f:
    data = f.read().split("\n\n")

seeds = [int(seed) for seed in data[0].replace("seeds: ", "").split()]
conditions = data[1:]
clean = [
    [[int(bit) for bit in item.split()] for item in sect.splitlines()[1:]]
    for sect in conditions
]


### FUNCTIONS
def expand_seeds(seeds):
    groups = [seeds[i : i + 2] for i in range(0, len(seeds), 2)]
    ranges = [[start, start + range - 1] for [start, range] in groups]
    return ranges


def map_ranges():
    maps = []
    for condition in clean:
        lsts = []
        for [destination, source, steps] in condition:
            start = source
            end = (source + steps) - 1
            diff = destination - source
            lsts.append([start, end, diff])
        maps.append(lsts)
    return maps


def break_seed(seed, rng):
    seed_start, seed_end = seed
    range_start, range_end, diff = rng
    if seed_start < range_start and range_start < seed_end <= range_end:
        return [[seed_start, range_start - 1], [range_start + diff, seed_end + diff]]
    elif range_start < seed_start < range_end and seed_end > range_end:
        return [[seed_start + diff, range_end + diff], [range_end + 1, seed_end]]
    elif seed_start < range_start and seed_end > range_end:
        return [
            [seed_start, range_start - 1],
            [range_start + diff, range_end + diff],
            [range_end + 1, seed_end],
        ]
    elif seed_start >= range_start and seed_end <= range_end:
        return [[seed_start + diff, seed_end + diff]]
    return []


def seed_after_round(seed, rnd):
    new_seed = seed
    for rng in rnd:
        new_seed = break_seed(seed, rng)
        if new_seed:
            return new_seed
    return new_seed


### RESULT PRESENTATION
def result_part_one():
    steppers = seeds.copy()
    maps = map_ranges()
    for m in maps:
        new_steppers = steppers.copy()
        for [start, end, diff] in m:
            for index, step in enumerate(steppers):
                if start <= step <= end:
                    new_steppers[index] += diff
        steppers = new_steppers
    return min(new_steppers)


def result_part_two():
    expanded_seeds = expand_seeds(seeds)
    maps = map_ranges()
    for m in maps:
        new_seeds = []
        for seed in expanded_seeds.copy():
            new_seed = seed_after_round(seed, m)
            for s in new_seed:
                new_seeds.append(s)
        expanded_seeds = new_seeds
    lowest = min([item[0] for item in expanded_seeds])
    return lowest


### DISPLAY RESULTS
print("Part 1:", result_part_one())
print("Part 2:", result_part_two())
