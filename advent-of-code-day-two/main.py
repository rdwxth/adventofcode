def load_input():
  with open("input.txt", "r") as rf:
      return [line.strip() for line in rf.readlines()]

def parse_game_data(lines):
  mr, mg, mb = 12, 13, 14
  data = []

  for line in lines:
      subsets = line.split(":")[1].split(';')
      game = [{pick.strip().split(" ")[1]: int(pick.strip().split(" ")[0]) for pick in turn.split(', ')} for turn in subsets]
      data.append(game)

  return data, mr, mg, mb

def part_one(data, mr, mg, mb):
  total = 0

  for i, game in enumerate(data):
      possible = all(
          not ('blue' in gs and gs['blue'] > mb) and
          not ('red' in gs and gs['red'] > mr) and
          not ('green' in gs and gs['green'] > mg)
          for gs in game
      )

      if possible:
          total += i + 1

  return total

def part_two(data):
  total = 0

  for game in data:
      max_r = max([turn['red'] if 'red' in turn else -1 for turn in game])
      max_b = max([turn['blue'] if 'blue' in turn else -1 for turn in game])
      max_g = max([turn['green'] if 'green' in turn else -1 for turn in game])
      total += max_r * max_b * max_g

  return total

def main():
  lines = load_input()
  data, mr, mg, mb = parse_game_data(lines)

  result_part_one = part_one(data, mr, mg, mb)
  result_part_two = part_two(data)

  print(f"Part 1: {result_part_one}")
  print(f"Part 2: {result_part_two}")

if __name__ == "__main__":
  main()
