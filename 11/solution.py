### PROCESS INPUT DATA
with open("input.txt", encoding="utf-8") as f:
    data = f.read().split("\n")


### FUNCTIONS
def get_indices_to_expand():
    cols_to_be_expanded = []
    rows_to_be_expanded = []
    for n in range(len(data[0])):
        if all([item == "." for item in [row[n] for row in data]]):
            cols_to_be_expanded.append(n)
    for n in range(len(data)):
        if all(item == "." for item in list(data[n])):
            rows_to_be_expanded.append(n)
    return cols_to_be_expanded, rows_to_be_expanded


def create_expanded_grid(data, step):
    cols_to_be_expanded, rows_to_be_expanded = get_indices_to_expand()
    grid = {}
    x_extras = 0
    for x, row in enumerate(data):
        y_extras = 0
        for y, item in enumerate(row):
            grid[(x + x_extras, y + y_extras)] = item
            if y in cols_to_be_expanded:
                y_extras += step
        if x in rows_to_be_expanded:
            x_extras += step
    return grid


def get_all_pairs(grid):
    current = 1
    numbers_dict = {}
    for key, item in grid.items():
        if item == "#":
            numbers_dict[current] = key
            current += 1
    return numbers_dict, [
        (i, j) for i in range(1, current) for j in range(i + 1, current)
    ]


def get_distances(grid):
    coords, pairs = get_all_pairs(grid)
    distances = [
        abs(coords[first][0] - coords[second][0])
        + abs(coords[first][1] - coords[second][1])
        for first, second in pairs
    ]
    return distances


### RESULT PRESENTATION
def result_part_one():
    grid = create_expanded_grid(data, 1)
    distances = get_distances(grid)
    return sum(distances)


def result_part_two():
    grid = create_expanded_grid(data, 999999)
    distances = get_distances(grid)
    return sum(distances)


### DISPLAY RESULTS
print("Part 1:", result_part_one())
print("Part 2:", result_part_two())
