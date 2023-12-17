### PROCESS INPUT DATA
with open("input.txt", encoding="utf-8") as f:
    data = f.read().splitlines()


### FUNCTIONS
def create_grid(data):
    grid = {}
    for x, row in enumerate(data):
        for y, item in enumerate(row):
            grid[(x, y)] = item
    return grid


def check_ahead(position, grid, direction):
    x, y = position
    NEIGHBORS = {
        "DOWN": (x + 1, y),
        "UP": (x - 1, y),
        "RIGHT": (x, y + 1),
        "LEFT": (x, y - 1),
    }
    next = NEIGHBORS[direction]
    return grid[next] if next in grid else None


def move_rock(position, grid, direction="UP"):
    new_grid = grid
    new_position = position
    while check_ahead(new_position, new_grid, direction) == ".":
        x, y = new_position
        NEIGHBORS = {
            "DOWN": (x + 1, y),
            "UP": (x - 1, y),
            "RIGHT": (x, y + 1),
            "LEFT": (x, y - 1),
        }
        next = NEIGHBORS[direction]
        new_grid[next] = "O"
        new_grid[new_position] = "."
        new_position = next
    return new_grid


def count_load(grid):
    total = 0
    bottom = list(grid.keys())[-1][0]
    for key, value in grid.items():
        if value == "O":
            total += bottom - key[0] + 1
    return total


def cycle(grid):
    new_grid = grid
    directions = ["UP", "LEFT", "DOWN", "RIGHT"]
    for direction in directions:
        for pos, item in (
            new_grid.items()
            if direction in ["UP", "LEFT"]
            else reversed(new_grid.items())
        ):
            if item == "O":
                new_grid = move_rock(pos, new_grid, direction)
    return new_grid


### RESULT PRESENTATION
def result_part_one():
    grid = create_grid(data)
    for pos, item in grid.items():
        if item == "O":
            grid = move_rock(pos, grid)
    return count_load(grid)


def result_part_two():
    grid = create_grid(data)
    seen = {}
    n = 0
    cycle_start = 0
    next_cycle_start = 0
    while "".join(grid.values()) not in seen:
        n += 1
        grid_key = "".join(grid.values())
        grid = cycle(grid)
        seen[grid_key] = grid
    cycle_start = n
    first_key = grid_key
    while True:
        n += 1
        grid = cycle(grid)
        if "".join(grid.values()) == first_key:
            break
    next_cycle_start = n + 1
    cycle_length = next_cycle_start - cycle_start
    modulo = (1000000000 - cycle_start) % cycle_length
    index = modulo + cycle_start
    grid = create_grid(data)
    for n in range(index):
        grid = cycle(grid)
    return count_load(grid)


### DISPLAY RESULTS
print("Part 1:", result_part_one())
print("Part 2:", result_part_two())
