
def get_input(input_file):
    input = []
    with open(file=input_file, mode="r", encoding="utf-8") as file:
        for line in file:
            input.append(line.strip())
    return input

def solve_part1(grid):
    number_of_splits = 0
    # Get the starting position (colum index)
    start_position = 0
    c = grid[0][start_position]
    while c != "S":
        start_position += 1
        c = grid[0][start_position]

    current_row = 1
    tachyon_columns = []
    tachyon_columns.append(start_position)

    for current_row in range(1, len(grid)):
        new_tachyon_columns = tachyon_columns.copy()
        for tachyon in tachyon_columns:
            if grid[current_row][tachyon] == "^":
                if tachyon - 1 not in new_tachyon_columns and tachyon - 1 >= 0:
                    new_tachyon_columns.append(tachyon - 1)
                if tachyon + 1 not in new_tachyon_columns and tachyon + 1 < len(grid[0]):
                    new_tachyon_columns.append(tachyon + 1)
                new_tachyon_columns.remove(tachyon)
                number_of_splits += 1
        tachyon_columns = new_tachyon_columns
    return number_of_splits

def main():
    input = get_input("input.txt")
    result = solve_part1(input)
    print(f"Part 1 result: {result}")
    
if __name__ == "__main__":
    main()