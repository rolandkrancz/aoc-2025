
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

def solve_part2(grid):
    start_position = grid[0].find("S")
    current_particles = {start_position: 1}

    for current_row in range(1, len(grid)):
        next_particles = {}
        for col, count in current_particles.items():
            if grid[current_row][col] == "^":
                if col - 1 >= 0:
                    next_particles[col - 1] = next_particles.get(col - 1, 0) + count
                if col + 1 < len(grid[0]):
                    next_particles[col + 1] = next_particles.get(col + 1, 0) + count
            else:
                next_particles[col] = next_particles.get(col, 0) + count

        current_particles = next_particles

    return sum(current_particles.values())

def main():
    data = get_input("input.txt")
    result = solve_part1(data)
    print(f"Part 1 result: {result}")
    result = solve_part2(data)
    print(f"Part 2 result: {result}")
    
if __name__ == "__main__":
    main()