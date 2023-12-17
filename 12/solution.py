### PROCESS INPUT DATA
with open("input.txt", encoding="utf-8") as f:
    data = [item.split() for item in f.read().splitlines()]

data = [[first, list(map(int, second.split(",")))] for first, second in data]


### FUNCTIONS
def check(condition_record, groups, seen_combinations):
    current_combination = (condition_record, tuple(groups))

    if current_combination in seen_combinations:
        return seen_combinations[current_combination]
    if not condition_record:
        return 1 if not groups else 0
    if not groups:
        return 0 if "#" in condition_record else 1

    combination_result = 0
    next_spring = condition_record[0]
    all_but_first = condition_record[1:]

    if next_spring == ".":
        combination_result += check(all_but_first, groups, seen_combinations)

    if next_spring == "#":
        limit = groups[0]
        if (
            len(condition_record) >= limit
            and "." not in condition_record[:limit]
            and (groups[0] == len(condition_record) or condition_record[limit] != "#")
        ):
            combination_result += check(
                condition_record[limit:], groups[1:], seen_combinations
            )
    if next_spring == "?":
        first_option = check("." + all_but_first, groups, seen_combinations)
        second_option = check("#" + all_but_first, groups, seen_combinations)
        combination_result += first_option + second_option

    if current_combination not in seen_combinations:
        seen_combinations[current_combination] = combination_result

    return combination_result


def result_part_one():
    return sum(check(condition_record, groups, {}) for condition_record, groups in data)


def result_part_two():
    return sum(
        check(((condition_record + "?") * 5)[:-1], groups * 5, {})
        for condition_record, groups in data
    )


print("Part 1:", result_part_one())
print("Part 2:", result_part_two())
