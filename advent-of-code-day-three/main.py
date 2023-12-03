from collections import defaultdict

def read_engine_schematic():
    file_path = "input.txt"
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file.readlines()]

def calculate_part_product(nums):
    """calc the product of part numbers that appear in pairs."""
    product = 0

    for values in nums.values():
        if len(values) == 2:
            product += values[0] * values[1]

    return product

if __name__ == "__main__":
    engine_schematic = read_engine_schematic()

    R, C = len(engine_schematic), len(engine_schematic[0])
    total_sum = 0
    nums = defaultdict(list)

    for r in range(R):
        gears = set()  # positions of '*' characters next to the current number
        n = 0
        has_part = False

        for c in range(C + 1):
            if c < C and engine_schematic[r][c].isdigit():
                n = n * 10 + int(engine_schematic[r][c])

                for rr in [-1, 0, 1]:
                    for cc in [-1, 0, 1]:
                        if 0 <= r + rr < R and 0 <= c + cc < C:
                            ch = engine_schematic[r + rr][c + cc]
                            if not ch.isdigit() and ch != '.':
                                has_part = True
                            if ch == '*':
                                gears.add((r + rr, c + cc))
            elif n > 0:
                for gear in gears:
                    nums[gear].append(n)
                if has_part:
                    total_sum += n
                n, has_part, gears = 0, False, set()

    print(f"The sum of all part numbers is: {total_sum}")

    # Part 2: Calculate the product of part numbers in pairs
    part_product = calculate_part_product(nums)
    print(f"The product of part numbers in pairs is: {part_product}")
