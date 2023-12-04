import sys
from collections import defaultdict

def read_input(filename):
    with open(filename) as file:
        return file.read().strip().split('\n')

def process_scratchcards(data):
    points = 0
    counts = defaultdict(int)

    for i, line in enumerate(data):
        counts[i] += 1
        first, rest = line.split('|')
        card_id, card_nums = first.split(':')
        card_nums = [int(x) for x in card_nums.split()]
        rest_nums = [int(x) for x in rest.split()]

        common_numbers = set(card_nums) & set(rest_nums)
        val = len(common_numbers)

        if val > 0:
            points += 2**(val - 1)

        for j in range(val):
            counts[i + 1 + j] += counts[i]

    return points, sum(counts.values())

if __name__ == "__main__":

    puzzle_input = read_input("input.txt")

    part1_score, total_score = process_scratchcards(puzzle_input)

    print("Part 1:", part1_score)
    print("Part 2:", total_score)
