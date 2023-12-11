### PROCESS INPUT DATA
with open("input.txt", encoding="utf-8") as f:
    data = [row + "." for row in f.read().splitlines()]


### FUNCTIONS
def create_grid(data):
    grid = {}
    for x, row in enumerate(data):
        for y, item in enumerate(row):
            grid[(x, y)] = item
    return grid


def get_grouped_coords(grid):
    collected_groups = []
    currently_collecting = []
    for coord, value in grid.items():
        if value.isdigit():
            currently_collecting.append(coord)
        elif currently_collecting:
            collected_groups.append(currently_collecting)
            currently_collecting = []
    return collected_groups


def get_eight_neighbors(position, grid):
    x, y = position
    neighboring_positions = [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
        (x + 1, y + 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
        (x - 1, y - 1),
    ]
    return [neighbor for neighbor in neighboring_positions if neighbor in grid]


def group_as_number(group, grid):
    return int("".join([grid[coord] for coord in group]))


def has_no_symbol_neighbors(grid, neighbors):
    for neighbor in neighbors:
        if grid[neighbor] != "." and not grid[neighbor].isdigit():
            return False
    return True


def get_group_neighbors(group, grid):
    neighbors = []
    for coord in group:
        neighbors += get_eight_neighbors(coord, grid)
    return list(set(neighbors))


### GLOBALS
GRID = create_grid(data)
NUMBERS = get_grouped_coords(GRID)
GEARS = [coord for coord, content in GRID.items() if content == "*"]


### RESULT PRESENTATION
def result_part_one():
    return sum(
        [
            group_as_number(group, GRID)
            for group in NUMBERS
            if not has_no_symbol_neighbors(GRID, get_group_neighbors(group, GRID))
        ]
    )


def result_part_two():
    neighbors_of_gears_with_two_neighbors = []
    for gear in GEARS:
        neighboring_numbers = list(
            set(
                [
                    group_as_number(num, GRID)
                    for num in NUMBERS
                    if set(num) & set(get_eight_neighbors(gear, GRID))
                ]
            )
        )
        if len(neighboring_numbers) == 2:
            neighbors_of_gears_with_two_neighbors.append(neighboring_numbers)
    return sum(
        [first * second for [first, second] in neighbors_of_gears_with_two_neighbors]
    )


### DISPLAY RESULTS
print("Part 1:", result_part_one())
print("Part 2:", result_part_two())
