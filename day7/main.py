
def get_input(input_file):
    with open(input_file, encoding="utf-8") as file:
        return [line.strip() for line in file]

def solve_part1(grid):
    number_of_splits = 0
    start_position = grid[0].find("S")
    tachyon_columns = {start_position}

    for current_row in range(1, len(grid)):
        new_tachyon_columns = tachyon_columns.copy()
        for tachyon in tachyon_columns:
            if grid[current_row][tachyon] == "^":
                if tachyon - 1 >= 0:
                    new_tachyon_columns.add(tachyon - 1)
                if tachyon + 1 < len(grid[0]):
                    new_tachyon_columns.add(tachyon + 1)
                new_tachyon_columns.discard(tachyon)
                number_of_splits += 1
        tachyon_columns = new_tachyon_columns
    return number_of_splits

def main():
    data = get_input("input.txt")
    result = solve_part1(data)
    print(f"Part 1 result: {result}")
    
if __name__ == "__main__":
    main()