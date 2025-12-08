import csv

def get_input(file):
    columns = []
    with open(file, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=" ", skipinitialspace=True)
        columns = list(zip(*reader))
    return columns

def solve_part1(columns):
    result = 0
    col_length = len(columns[0])

    for col in columns:
        col_result = 0
        operation = col[col_length-1]
        for i in range(0, col_length-1):
            if operation == "+":
                col_result += int(col[i])
            elif operation == "*":
                if not col_result:
                    col_result = int(col[i])
                else:
                    col_result *= int(col[i])
        result += col_result

    return result

def solve_part2(file):
    result = 0
    with open(file, mode="r", encoding="utf-8") as f:
        lines = f.readlines()
        number_of_lines = len(lines)
        length_of_line = len(lines[0])

        # Collect the numbers per column
        col_numbers = []
        for col in range(length_of_line-2, -1, -1):
            curr_char = ""
            col_number = ""
            for row in range(0, number_of_lines):
                curr_char = lines[row][col]
                if curr_char != " " and curr_char != "+" and curr_char != "*":
                    col_number += curr_char
            if col_number:
                col_number = int(col_number)
                col_numbers.append(col_number)
            # if an operator is found, do the math and empty the collected numbers
            if curr_char == "+":
                for num in col_numbers:
                    result += int(num)
                col_numbers = []
            elif curr_char == "*":
                multiplication_result = 1
                for num in col_numbers:
                    multiplication_result *= num
                result += multiplication_result
                col_numbers = []

    return result

def main():
    columns = get_input("test_input.txt")
    result = solve_part1(columns)
    print(f"Part 1 result: {result}")

    result = solve_part2("input.txt")
    print(f"Part 2 result: {result}")

if __name__ == "__main__":
    main()
