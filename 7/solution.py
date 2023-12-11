from collections import Counter

### PROCESS INPUT DATA
with open("input.txt", encoding="utf-8") as f:
    data = [
        [list(bit[0]), int(bit[1])]
        for bit in [line.split() for line in f.read().splitlines()]
    ]

### GLOBALS
FIRST_ORDER = "23456789TJQKA"
SECOND_ORDER = "J23456789TQKA"


### FUNCTIONS
def hand_as_values(hand, order):
    return [order.index(item) for item in hand]


def get_formation(hand, use_jokers):
    jokers = 0
    if use_jokers:
        hand = [card for card in hand if card != "J"]
        jokers = 5 - len(hand)

    card_counts = list(Counter(hand).values())
    if not card_counts:
        card_counts = [0]
    max_count = max(card_counts)

    if 5 in card_counts or max_count + jokers == 5:
        return 7
    elif 4 in card_counts or max_count + jokers == 4:
        return 6
    elif (3 in card_counts and 2 in card_counts) or (
        card_counts.count(2) == 2 and jokers == 1
    ):
        return 5
    elif 3 in card_counts or max_count + jokers == 3:
        return 4
    elif card_counts.count(2) == 2:
        return 3
    elif 2 in card_counts or max_count + jokers == 2:
        return 2
    else:
        return 1


def sort_and_count(using_jokers, order, hands):
    sorted_lines = sorted(
        hands,
        key=lambda x: (get_formation(x[0], using_jokers), *hand_as_values(x[0], order)),
    )
    total = 0
    for index, h in enumerate(sorted_lines):
        total += (index + 1) * h[1]
    return total


### RESULT PRESENTATION
def result_part_one():
    return sort_and_count(False, FIRST_ORDER, data)


def result_part_two():
    return sort_and_count(True, SECOND_ORDER, data)


### DISPLAY RESULTS
print("Part 1:", result_part_one())
print("Part 2:", result_part_two())
