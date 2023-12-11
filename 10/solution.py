### PROCESS INPUT DATA
with open("input.txt", encoding="utf-8") as f:
    data = f.read().split("\n")


### FUNCTIONS
def create_grid(data):
    grid = {}
    for x, row in enumerate(data):
        for y, item in enumerate(row):
            grid[(x, y)] = item
    return grid


def find_starting_point(grid):
    for key, value in grid.items():
        if value == "S":
            return key


def get_four_neighbors(position, grid):
    x, y = position
    neighboring_positions = [(x + 1, y), (x, y + 1), (x, y - 1), (x - 1, y)]
    return [neighbor for neighbor in neighboring_positions if neighbor in grid]


def get_first_step(position, grid):
    down, right, left, _ = get_four_neighbors(position, grid)

    directions = {
        down: {"|": (down, "DOWN"), "J": (down, "LEFT"), "L": (down, "RIGHT")},
        right: {"-": (right, "RIGHT"), "J": (right, "UP"), "7": (right, "DOWN")},
        left: {"-": (left, "LEFT"), "F": (left, "DOWN"), "L": (left, "UP")},
    }

    for item in [down, right, left]:
        if grid[item] in directions[item]:
            return directions[item][grid[item]]


def get_next_position(position, direction, grid):
    x, y = position
    positions = {
        "UP": (x - 1, y),
        "DOWN": (x + 1, y),
        "LEFT": (x, y - 1),
        "RIGHT": (x, y + 1),
    }
    directions = {
        "UP": {"|": "UP", "7": "LEFT", "F": "RIGHT"},
        "DOWN": {"|": "DOWN", "J": "LEFT", "L": "RIGHT"},
        "LEFT": {"F": "DOWN", "L": "UP", "-": "LEFT"},
        "RIGHT": {"7": "DOWN", "J": "UP", "-": "RIGHT"},
    }
    next_position = positions[direction]
    new_direction = directions[direction].get(grid[next_position], None)
    return next_position, new_direction


def get_enclosure(grid):
    starting_point = find_starting_point(grid)
    enclosure = [starting_point]
    current_position, direction = get_first_step(starting_point, grid)
    enclosure.append(current_position)
    while current_position != starting_point:
        current_position, direction = get_next_position(
            current_position, direction, grid
        )
        enclosure.append(current_position)
    return enclosure


def count_inside_points(grid_row, enclosure_row, grid):
    row = "".join([grid[num] if num in enclosure_row else "." for num in grid_row])
    replaced = list(row.replace("-", "").replace("FJ", "|").replace("L7", "|"))
    total = 0
    for index, item in enumerate(replaced):
        if item == ".":
            left = len([item for item in replaced[:index] if item == "|"])
            right = len([item for item in replaced[index + 1 :] if item == "|"])
            if left % 2 != 0 and right % 2 != 0:
                total += 1
    return total


### GLOBALS
GRID = create_grid(data)
ENCLOSURE = get_enclosure(GRID)


### RESULT PRESENTATION
def result_part_one():
    return len(ENCLOSURE) // 2


def result_part_two():
    total = 0
    for line_number in range(len(data)):
        coords = [coord for coord in GRID if coord[0] == line_number]
        relevant_enclosure_values = [
            coord for coord in ENCLOSURE if coord[0] == line_number
        ]
        total += count_inside_points(coords, relevant_enclosure_values, GRID)
    return total


### DISPLAY RESULTS
print("Part 1:", result_part_one())
print("Part 2:", result_part_two())
