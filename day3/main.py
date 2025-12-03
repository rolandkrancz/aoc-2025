
def solve_part1(input_file):
    with open(input_file, "r", encoding="utf-8") as file:
        total_jolts = 0
        for line in file:
            jolts = 0
            digits_of_line = []
            for char in line.strip():
                digits_of_line.append(int(char))

            highest_digit_index = _find_highest_digit_index(digits_of_line)
            highest_digit = digits_of_line.pop(highest_digit_index)

            if highest_digit_index < len(digits_of_line):
                # There are digits to the right - search there to get the highest value
                digits_to_right = digits_of_line[highest_digit_index:]
                index = _find_highest_digit_index(digits_to_right)
                highest_right = digits_to_right[index]
                jolts = highest_digit*10 + highest_right
            else:
                # No digits to the right - search highest value to the left
                digits_to_left = digits_of_line[:highest_digit_index]
                index = _find_highest_digit_index(digits_to_left)
                highest_left = digits_to_left[index]
                jolts = highest_left*10 + highest_digit

            total_jolts += jolts

    return total_jolts

def _find_highest_digit_index(digits):
    highest_digit = -1
    highest_digit_index = -1

    for index, digit in enumerate(digits):
        if digit > highest_digit:
            highest_digit = digit
            highest_digit_index = index

    return highest_digit_index

def solve_part2(input_file):
    with open(input_file, "r", encoding="utf-8") as file:
        total_jolts = 0
        for line in file:
            digits_of_line = []
            for char in line.strip():
                digits_of_line.append(int(char))
            
            # Greedy algorithm with stack
            to_remove = len(digits_of_line) - 12
            stack = []
            for digit in digits_of_line:
                while to_remove and stack and digit > stack[-1]:
                    stack.pop()
                    to_remove -= 1
                stack.append(digit)

            jolts = int("".join(map(str, stack[:12]))) 
            total_jolts += jolts

    return total_jolts

def main():
    result = solve_part1("input.txt")
    print(f"Part 1 result: {result}")

    result = solve_part2("input.txt")
    print(f"Part 2 result: {result}")

    return 0

if __name__ == "__main__":
    main()
