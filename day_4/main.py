total_points = 0
total_scratchcards = 0
scratch_cards = []

class card:
    def __init__(self, id, card_nums):
        self.id = id
        self.card_nums = card_nums
        self.copies = 1

def process_input(line):
    split1 = line.strip().split(": ")
    card_split = split1[1].split(" | ")
    card_list = []

    for cards in card_split:
        card_nums = cards.split(' ')
        card_nums = list(map(lambda x: int(x) if x != '' else None, card_nums))
        card_nums = [x for x in card_nums if x != None]

        card_list.append(card_nums)

    return card_list

def get_points(card):
    matches = 0
    for winning_num in card[0]:
        if winning_num in card[1]:
            matches += 1

    points = 0
    if matches > 0:
        points = 1
        for _ in range(matches - 1):
            points *= 2

    return points, matches

with open("input.txt") as f:
    for card_num, line in enumerate(f):
        card_item = process_input(line)
        new_card = card(card_num + 1, card_item)

        scratch_cards.append(new_card)

for card_num, card_item in enumerate(scratch_cards):
    card_points, matches = get_points(card_item.card_nums, card_item.copies)
    total_points += card_points
    
    if matches > 0:
        for i in range(card_num + 1, card_num + matches + 1):
            try:
                scratch_cards[i].copies += card_item.copies
            except IndexError:
                break
    
    print(f"Card {card_item.id}: {card_item.card_nums} Points = {card_points}, with {card_item.copies} copies.") 

for card_item in scratch_cards:
    total_scratchcards += card_item.copies

print("\n-------------------------------")
print(f"Total winnings: {total_points}, with {total_scratchcards} cards.")
