### PROCESS INPUT DATA
with open("input.txt") as f:
    data = [row.replace("Game ", "").split(": ") for row in f.read().splitlines()]


def parse_row(row):
    return [
        {item.split(" ")[1]: int(item.split(" ")[0]) for item in lst} for lst in row
    ]


rounds = {}
for row in data:
    rounds[row[0]] = parse_row([item.split(", ") for item in row[1].split("; ")])

### GLOBALS
BAG = {"red": 12, "green": 13, "blue": 14}


### FUNCTIONS
def calculate_round(dct):
    round_dict = {"red": 0, "green": 0, "blue": 0}
    for round_data in dct:
        for color, amount in round_data.items():
            if amount > round_dict[color]:
                round_dict[color] = amount
    return round_dict["red"] * round_dict["green"] * round_dict["blue"]


### RESULT PRESENTATION
def result_part_one():
    possible = [
        int(key)
        for key, value in rounds.items()
        if all(
            amount <= BAG[color] for round in value for color, amount in round.items()
        )
    ]
    return sum(possible)


def result_part_two():
    return sum([calculate_round(value) for value in rounds.values()])


### DISPLAY RESULTS
print("Part 1:", result_part_one())
print("Part 2:", result_part_two())
