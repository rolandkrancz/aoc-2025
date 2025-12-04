def solve_part1(input_file):
    accessible_rolls = 0
    with open(input_file, "r", encoding="utf-8") as file:
        grid = [list(line.strip()) for line in file]

    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == "@":
                adjacent_rolls = _count_adjacent_rolls(grid, x, y)
                if adjacent_rolls < 4:
                    accessible_rolls += 1

    return accessible_rolls

def _count_adjacent_rolls(grid, x, y):
    number_of_adjacent_rolls = 0
    adjacent_positions = [[x-1, y-1], [x+1, y-1], [x, y-1],
                          [x-1, y],              [x+1, y],
                          [x-1, y+1], [x+1, y+1], [x, y+1]]

    for coordinates in adjacent_positions:
        current_x = coordinates[0]
        current_y = coordinates[1]
        if 0 <= current_x < len(grid) and 0 <= current_y < len(grid[current_x]):
            if grid[current_x][current_y] == "@":
                number_of_adjacent_rolls += 1

    return number_of_adjacent_rolls

def main():
    print(solve_part1("input.txt"))
    return 0

if __name__ == "__main__":
    main()