### PROCESS INPUT first
with open("input.txt", encoding="utf-8") as f:
    input = f.read().splitlines()

first = [[int(item) for item in part.split(": ")[1].strip().split()] for part in input]
second = [int(part.split(": ")[1].strip().replace(" ", "")) for part in input]


### FUNCTIONS
def list_record_distances(time, distance):
    distances = []
    for n in range(0, time + 1):
        race_distance = n * (time - n)
        if race_distance > distance:
            distances.append(race_distance)
    return len(distances)


def list_by_index(time_list, distance_list):
    return [[time_list[i], distance_list[i]] for i in range(len(time_list))]


### RESULT PRESENTATION
def result_part_one():
    time, distance = first
    paired_list = list_by_index(time, distance)
    amounts = 1
    for time, distance in paired_list:
        amounts *= list_record_distances(time, distance)
    return amounts


def result_part_two():
    time, distance = second
    return list_record_distances(time, distance)


### DISPLAY RESULTS
print("Part 1:", result_part_one())
print("Part 2:", result_part_two())
