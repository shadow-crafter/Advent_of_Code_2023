hands = []

CARD_STRENGTHS = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
TYPE_STRENGTHS = ['FIVE', 'FOUR', 'FULL', 'THREE', 'TWO', 'ONE', 'HIGH']

class hand:
    def __init__(self, cards: str, bid: int, hand_type: str):
        self.cards = cards
        self.bid = bid
        self.type = hand_type
        self.rank = 1

def process_input(line):
    cards, bid = line.split(' ')
    return cards, int(bid)

def get_type(cards):
    matches = []

    counter = {}
    for c in cards:
        counter[c] = counter.get(c, 0) + 1
    vals = sorted(counter.items(), key=lambda x:x[1], reverse=True)

    most_occuring = vals[0][0]
    if most_occuring != 'J':
        cards = cards.replace('J', most_occuring)
    else:
        try:
            cards = cards.replace('J', vals[1][0])
        except IndexError:
            pass

    for card in cards:
        if cards.count(card) == 5:
            return 'FIVE'
        elif cards.count(card) == 4:
            return 'FOUR'
        elif cards.count(card) == 3:
            filtered = cards.replace(card, '')
            if cards.count(filtered[0]) == 2:
                return 'FULL'
            else:
                return 'THREE'
        else:
            if cards.count(card) > 1 and not card in matches:
                matches.append(card)
    
    if len(matches) == 2:
        return 'TWO'
    elif len(matches) == 1:
        return 'ONE'
    else:
        return 'HIGH'

def win_check(card1: hand, card2: hand) -> bool:
    if TYPE_STRENGTHS.index(card1.type) < TYPE_STRENGTHS.index(card2.type):
        return True
    elif TYPE_STRENGTHS.index(card1.type) > TYPE_STRENGTHS.index(card2.type):
        return False
    else:
        for i, c in enumerate(card1.cards):
            if CARD_STRENGTHS.index(c) < CARD_STRENGTHS.index(card2.cards[i]):
                return True
            elif CARD_STRENGTHS.index(c) > CARD_STRENGTHS.index(card2.cards[i]):
                return False
            else:
                continue
    raise Exception("Tie")

with open("input.txt") as f:
    for line in f:
        cards, bid = process_input(line)
        card_type = get_type(cards)
        new_hand = hand(cards, bid, card_type)

        hands.append(new_hand)

        if 'J' in cards:
            print(f"Cards: {cards}, with the type {card_type}")

print("\n. . .\n") #spacer

for deck1 in hands:
    for deck2 in hands:
        if deck2 is deck1:
            continue
        
        win = win_check(deck1, deck2)
        if win:
            deck1.rank += 1

winnings = []
for deck in hands:
    print(f"{deck.cards}: {deck.rank}")
    winnings.append(deck.bid * deck.rank)

print(f"\nTOTAL WINNINGS: {sum(winnings)}")
