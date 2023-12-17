### PROCESS INPUT DATA
with open("input.txt", encoding="utf-8") as f:
    data = f.read().split(",")


### FUNCTIONS
def calculate_hash(str):
    value = 0
    for char in str:
        value = ((value + ord(char)) * 17) % 256
    return value


def get_op_and_hash(str):
    if "=" in str:
        label, num = str.split("=")
        return calculate_hash(label), (label, int(num)), "REPLACE"
    if "-" in str:
        str = str.replace("-", "")
        return calculate_hash(str), str, "REMOVE"


def calc_focusing_power(boxes):
    total = 0
    for num, content in boxes.items():
        for i, item in enumerate(content):
            total += (num + 1) * (i + 1) * item[1]
    return total


### RESULT PRESENTATION
def result_part_one():
    return sum(calculate_hash(str) for str in data)


def result_part_two():
    boxes = {}
    for str in data:
        box, label, operation = get_op_and_hash(str)
        if operation == "REMOVE" and box in boxes:
            boxes[box] = [lens for lens in boxes[box] if lens[0] != label]
        if operation == "REPLACE":
            if box not in boxes:
                boxes[box] = [label]
            else:
                found = False
                for index, lens in enumerate(boxes[box]):
                    if lens[0] == label[0]:
                        found = True
                        boxes[box][index] = label
                if not found:
                    boxes[box].append(label)
    return calc_focusing_power(boxes)


### DISPLAY RESULTS
print("Part 1:", result_part_one())
print("Part 2:", result_part_two())
