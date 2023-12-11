### PROCESS INPUT DATA
with open("input.txt", encoding="utf-8") as f:
    data = [[int(item) for item in part.split()] for part in f.read().splitlines()]


### FUNCTIONS
def get_next(lst):
    return [item - lst[i - 1] for i, item in enumerate(lst[1:], 1)]


def expand_line(line):
    expanded = [line]
    while not all(item == 0 for item in expanded[-1]):
        expanded.append(get_next(expanded[-1]))
    return expanded


def get_last(line):
    expanded = list(reversed(expand_line(line)))
    for i, l in enumerate(expanded[1:], 1):
        l.append(l[-1] + expanded[i - 1][-1])
    return expanded[-1][-1]


### RESULT PRESENTATION
def result_part_one():
    return sum([get_last(line) for line in data])


def result_part_two():
    return sum([get_last(line[::-1]) for line in data])


### DISPLAY RESULTS
print("Part 1:", result_part_one())
print("Part 2:", result_part_two())
