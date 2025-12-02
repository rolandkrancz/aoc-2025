
def solve(input_file, part):
    invalid_ids = []
    with open(input_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            id_ranges = line.split(",")

            for id_range in id_ranges:
                ids = id_range.split("-")
                start_id = int(ids[0])
                end_id = int(ids[1])
                invalid_ids_in_range = _get_invalid_ids_in_range(start_id, end_id, part)
                invalid_ids.extend(invalid_ids_in_range)

    return sum(invalid_ids)

def _get_invalid_ids_in_range(start_id, end_id, part):
    invalid_ids = []
    for current_id in range(start_id, end_id + 1):
        if part == 1:
            if _is_invalid_id_part1(current_id):
                invalid_ids.append(current_id)
        elif part == 2:
            if _is_invalid_id_part2(current_id):
                invalid_ids.append(current_id)

    return invalid_ids

def _is_invalid_id_part1(current_id):
    id_string = str(current_id)
    midpoint = len(id_string) // 2
    id_string_first_half = id_string[:midpoint]
    id_string_second_half = id_string[midpoint:]

    return bool(id_string_first_half == id_string_second_half)

def _is_invalid_id_part2(current_id):
    id_string = str(current_id)
    total_length = len(id_string)
    for sequence_length in range(1, total_length // 2 + 1):
        if total_length % sequence_length == 0:
            sequence = id_string[:sequence_length]
            if sequence * (total_length // sequence_length) == id_string:
                return True
    return False

def main():
    result = solve("input.txt", 1)
    print(f"Part 1 Result: {result}")
    
    result = solve("input.txt", 2)
    print(f"Part 2 Result: {result}")

if __name__ == "__main__":
    main()