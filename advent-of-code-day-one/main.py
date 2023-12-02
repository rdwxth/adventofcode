def find_all_occurrences(a_str, sub):
  start = 0
  while True:
      start = a_str.find(sub, start)
      if start == -1:
          return
      yield start
      start += len(sub)  # use start += 1 to find overlapping matches

def extract_calibration_values(lines):
  no_str = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
  total_sum = 0

  for line in lines:
      found = []
      for k, c in enumerate(line):
          if c.isnumeric():
              found.append((k, int(c)))
      for j, no_rep in enumerate(no_str):
          for idx in find_all_occurrences(line, no_rep):
              found.append((idx, j + 1))

      found.sort()
      total_sum += int(str(found[0][1]) + str(found[-1][1]))

  return total_sum

def main():
  with open("input.txt", "r+") as rf:
      lines = [line.strip() for line in rf.readlines()]

  result = extract_calibration_values(lines)
  print("The sum of all calibration values is:", result)

if __name__ == "__main__":
  main()
