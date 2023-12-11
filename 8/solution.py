import math

### PROCESS INPUT DATA
with open("input.txt", encoding="utf-8") as f:
    instruction, moves = f.read().split("\n\n")

instruction = "".join(["0" if item == "L" else "1" for item in instruction])
moves = [
    (item[0], item[1][1:-1].split(", "))
    for item in (item.split(" = ") for item in moves.splitlines())
]

moves_dict = {}
for move in moves:
    moves_dict[move[0]] = move[1]

### GLOBALS


### FUNCTIONS
def get_moves(start, target, part):
    current = start
    moves = 0
    while (current != target and part == 1) or (current[-1] != target and part == 2):
        for i in instruction:
            moves += 1
            current = moves_dict[current][int(i)]
    return moves


### RESULT PRESENTATION
def result_part_one():
    return get_moves("AAA", "ZZZ", 1)


def result_part_two():
    starting_points = [move for move in moves_dict if move[-1] == "A"]
    cycle_lengths = [get_moves(move, "Z", 2) for move in starting_points]
    return math.lcm(*cycle_lengths)


### DISPLAY RESULTS
print("Part 1:", result_part_one())
print("Part 2:", result_part_two())
