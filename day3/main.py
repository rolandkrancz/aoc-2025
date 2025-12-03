
def solve(input_file):
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()
        total_jolts = 0
        for line in lines:
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

def main():
    result = solve("input.txt")
    print(f"Part 1 result: {result}")
    return 0


if __name__ == "__main__":
    main()
