### PROCESS INPUT DATA
def get_initial_data():
    with open("input.txt", encoding="utf-8") as f:
        data = [item.split(": ") for item in f.read().replace("Card ", "").splitlines()]
    cards = {}
    copies = {}
    for [num, content] in data:
        card_number = num.strip()
        cards[card_number] = [part.split() for part in content.split(" | ")]
        copies[card_number] = 1
    return cards, copies


### FUNCTIONS
def calculate():
    cards, copies = get_initial_data()
    points = 0
    for card_number, [numbers_on_card, winning_numbers] in cards.items():
        number_of_matches = len(set(numbers_on_card) & set(winning_numbers))
        for n in range(1, number_of_matches + 1):
            next_card = str(int(card_number) + n)
            if next_card in copies:
                copies[next_card] += copies[card_number]
        if number_of_matches > 0:
            points += 2 ** (number_of_matches - 1)
    return points, sum(copies.values())


### RESULT PRESENTATION
POINTS, TOTAL_COPIES = calculate()


def result_part_one():
    return POINTS


def result_part_two():
    return TOTAL_COPIES


### DISPLAY RESULTS
print("Part 1:", result_part_one())
print("Part 2:", result_part_two())
