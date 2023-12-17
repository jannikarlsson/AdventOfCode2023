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


def get_next_step(position, grid, direction):
    x, y = position
    NEIGHBORS = {
        "DOWN": (x + 1, y),
        "UP": (x - 1, y),
        "RIGHT": (x, y + 1),
        "LEFT": (x, y - 1),
    }
    return NEIGHBORS[direction] if NEIGHBORS[direction] in grid else None


def change_direction(position, grid, direction):
    item = grid[position]
    if item == ".":
        return [(get_next_step(position, grid, direction), direction)]
    if item == "-":
        if direction in ["RIGHT", "LEFT"]:
            return [(get_next_step(position, grid, direction), direction)]
        if direction in ["UP", "DOWN"]:
            directions = ["RIGHT", "LEFT"]
            return [
                (get_next_step(position, grid, direc), direc) for direc in directions
            ]
    if item == "|":
        if direction in ["UP", "DOWN"]:
            return [(get_next_step(position, grid, direction), direction)]
        if direction in ["LEFT", "RIGHT"]:
            directions = ["UP", "DOWN"]
            return [
                (get_next_step(position, grid, direc), direc) for direc in directions
            ]
    if item == "/":
        directions = {
            "DOWN": "LEFT",
            "UP": "RIGHT",
            "LEFT": "DOWN",
            "RIGHT": "UP",
        }
        return [
            (
                get_next_step(position, grid, directions[direction]),
                directions[direction],
            )
        ]
    if item == "\\":
        directions = {
            "DOWN": "RIGHT",
            "UP": "LEFT",
            "LEFT": "UP",
            "RIGHT": "DOWN",
        }
        return [
            (
                get_next_step(position, grid, directions[direction]),
                directions[direction],
            )
        ]


def get_all_starting_positions(grid):
    x_values = [coord[0] for coord in grid.keys()]
    y_values = [coord[1] for coord in grid.keys()]

    min_x, max_x = min(x_values), max(x_values)
    min_y, max_y = min(y_values), max(y_values)

    right_edge = [((x, max_y), "LEFT") for x in range(min_x, max_x + 1)]
    left_edge = [((x, min_y), "RIGHT") for x in range(min_x, max_x + 1)]
    top_edge = [((min_x, y), "DOWN") for y in range(min_y, max_y + 1)]
    bottom_edge = [((max_x, y), "UP") for y in range(min_y, max_y + 1)]

    return top_edge + bottom_edge + left_edge + right_edge


def get_sums(grid, all_positions):
    sums = []
    for position in all_positions:
        energized = {}
        seen = {}
        for key in grid:
            energized[key] = False
        queue = [position]
        while len(queue) > 0:
            position, direction = queue.pop()
            comp_key = (direction, position)
            if position is not None and comp_key not in seen:
                energized[position] = True
                queue += [
                    step
                    for step in change_direction(position, grid, direction)
                    if step[0] is not None
                ]
                seen[comp_key] = True
        sums.append(sum(1 for value in energized.values() if value is True))
    return sums


### RESULT PRESENTATION
def result_part_one():
    grid = create_grid(data)
    position = (0, 0)
    direction = "RIGHT"
    all_positions = [(position, direction)]
    return max(get_sums(grid, all_positions))


def result_part_two():
    grid = create_grid(data)
    all_positions = get_all_starting_positions(grid)
    return max(get_sums(grid, all_positions))


### DISPLAY RESULTS
print("Part 1:", result_part_one())
print("Part 2:", result_part_two())
