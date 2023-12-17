### PROCESS INPUT DATA
with open("input.txt", encoding="utf-8") as f:
    data = f.read().split("\n\n")


### FUNCTIONS
def flip_grid(grid):
    return ["".join(column) for column in zip(*grid.splitlines())]


def find_mirror(grid):
    mirror = (-1, -1)
    for index, row in enumerate(grid):
        if index < len(grid) - 1 and row == grid[index + 1]:
            mirror = (index, index + 1)
        prev, nxt = mirror
        while prev > 0 and nxt < len(grid) - 1:
            prev, nxt = prev - 1, nxt + 1
            if grid[prev] != grid[nxt]:
                mirror = (-1, -1)
        if mirror != (-1, -1):
            return mirror[1]
    return mirror[1]


def find_smudged_mirror(grid):
    mirror = (-1, -1)
    lifeline = True
    for index, row in enumerate(grid):
        if index < len(grid) - 1:
            if row == grid[index + 1]:
                mirror = (index, index + 1)
            elif is_one_off(row, grid[index + 1]):
                mirror = (index, index + 1)
                lifeline = False
        prev, nxt = mirror
        while prev > 0 and nxt < len(grid) - 1:
            prev, nxt = prev - 1, nxt + 1
            if grid[prev] != grid[nxt]:
                if lifeline and is_one_off(grid[prev], grid[nxt]):
                    lifeline = False
                else:
                    mirror = (-1, -1)
                    lifeline = True
        if mirror != (-1, -1):
            if lifeline:
                mirror = (-1, -1)
            else:
                return mirror[1]
    return mirror[1]


def is_one_off(first, second):
    diffs = [index for index, a in enumerate(first) if a != second[index]]
    return True if len(diffs) == 1 else False


def get_grid_sum(horizontal, vertical):
    return horizontal * 100 if horizontal > 0 else vertical


### RESULT PRESENTATION
def result_part_one():
    return sum(
        get_grid_sum(find_mirror(grid.splitlines()), find_mirror(flip_grid(grid)))
        for grid in data
    )


def result_part_two():
    return sum(
        get_grid_sum(
            find_smudged_mirror(grid.splitlines()), find_smudged_mirror(flip_grid(grid))
        )
        for grid in data
    )


### DISPLAY RESULTS
print("Part 1:", result_part_one())
print("Part 2:", result_part_two())
