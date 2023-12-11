import re

### PROCESS INPUT DATA
with open("input.txt", encoding="utf-8") as f:
    data = f.read().splitlines()

### GLOBALS
NUMBERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


### RESULT PRESENTATION
def result_part_one():
    digits = [[int(ch) for ch in row if ch.isdigit()] for row in data]
    return sum([int(str(item[0]) + str(item[-1])) for item in digits])


def result_part_two():
    regex = r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))"
    return sum(
        [
            int("".join(str(NUMBERS.get(item, item)) for item in [lst[0], lst[-1]]))
            for lst in [re.findall(regex, line) for line in data]
        ]
    )


### DISPLAY RESULTS
print("Part 1:", result_part_one())
print("Part 2:", result_part_two())
