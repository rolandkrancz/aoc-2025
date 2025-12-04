def get_input(input_file):
    grid = 0
    with open(input_file, "r", encoding="utf-8") as file:
        grid = [list(line.strip()) for line in file]
    return grid

def solve_part1(grid):
    accessible_rolls = 0

    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == "@":
                adjacent_rolls = _count_adjacent_rolls(grid, x, y)
                if adjacent_rolls < 4:
                    accessible_rolls += 1

    return accessible_rolls

def solve_part2(grid):
    prev_accessible_rolls = -1
    accessible_rolls = 0

    while accessible_rolls > prev_accessible_rolls:
        prev_accessible_rolls = accessible_rolls
        accessible_rolls += _iterate(grid)

    return accessible_rolls

def _iterate(grid):
    accessible_rolls = 0
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == "@":
                adjacent_rolls = _count_adjacent_rolls(grid, x, y)
                if adjacent_rolls < 4:
                    accessible_rolls += 1
                    grid[x][y] = "x"

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
    grid = get_input("input.txt")

    result = solve_part1(grid)
    print(f"Part 1 result: {result}")
    result = solve_part2(grid)
    print(f"part 2 result: {result}")

    return 0

if __name__ == "__main__":
    main()