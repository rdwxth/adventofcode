import sys
from collections import Counter

def read_input(filename):
    with open(filename) as file:
        data = file.read().strip().split('\n')
    return [tuple(line.split()) for line in data]

def transform_hand(hand, part2):
    replacements = {'T': chr(ord('9')+1), 'J': chr(ord('2')-1) if part2 else chr(ord('9')+2),
                    'Q': chr(ord('9')+3), 'K': chr(ord('9')+4), 'A': chr(ord('9')+5)}

    for old, new in replacements.items():
        hand = hand.replace(old, new)

    return hand

def calculate_strength(hand, part2):
    hand = transform_hand(hand, part2)
    card_counts = Counter(hand)

    if part2:
        target = max(card_counts, key=card_counts.get)
        for card in card_counts:
            if card != '1' and (card_counts[card] > card_counts[target] or target == '1'):
                target = card

        assert target != '1' or list(card_counts.keys()) == ['1']
        if '1' in card_counts and target != '1':
            card_counts[target] += card_counts['1']
            del card_counts['1']
        assert '1' not in card_counts or list(card_counts.keys()) == ['1'], f'{card_counts} {hand}'

    sorted_counts = sorted(card_counts.values())

    if sorted_counts == [5]:
        return (10, hand)
    elif sorted_counts == [1, 4]:
        return (9, hand)
    elif sorted_counts == [2, 3]:
        return (8, hand)
    elif sorted_counts == [1, 1, 3]:
        return (7, hand)
    elif sorted_counts == [1, 2, 2]:
        return (6, hand)
    elif sorted_counts == [1, 1, 1, 2]:
        return (5, hand)
    elif sorted_counts == [1, 1, 1, 1, 1]:
        return (4, hand)
    else:
        assert False, f'{card_counts} {hand} {sorted_counts}'

def main():
    filename = "input.txt"
    lines = read_input(filename)

    for part2 in [False, True]:
        hands_and_bids = [(hand, bid) for hand, bid in lines]
        sorted_hands_and_bids = sorted(hands_and_bids, key=lambda hb: calculate_strength(hb[0], part2))

        total_score = sum((i + 1) * int(bid) for i, (hand, bid) in enumerate(sorted_hands_and_bids))
        print(total_score)

if __name__ == "__main__":
    main()
