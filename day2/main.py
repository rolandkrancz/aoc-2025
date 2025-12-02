def solve_part1(input_file):
    invalid_ids = []
    with open(input_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            id_ranges = line.split(",")

            for id_range in id_ranges:
                ids = id_range.split("-")
                start_id = int(ids[0])
                end_id = int(ids[1])
                invalid_ids_in_range = _get_invalid_ids_in_range(start_id, end_id)
                invalid_ids.extend(invalid_ids_in_range)

    return sum(invalid_ids)

def _get_invalid_ids_in_range(start_id, end_id):
    invalid_ids = []
    for current_id in range(start_id, end_id + 1):
        id_string = str(current_id)
        midpoint = len(id_string) // 2
        id_string_first_half = id_string[:midpoint]
        id_string_second_half = id_string[midpoint:]

        if id_string_first_half == id_string_second_half:
            invalid_ids.append(current_id)

    return invalid_ids

def main():
    result = solve_part1("input.txt")
    print(f"Part 1 Result: {result}")

if __name__ == "__main__":
    main()