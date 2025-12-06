
def main():
    ingredients, ranges = get_input()
    
    result = solve_part1(ingredients, ranges)
    print(f"Part 1 result: {result}")
    result = solve_part2(ranges)
    print(f"Part 2 result: {result}")

def get_input():
    ranges = []
    ingredients = []
    
    with open("input.txt", mode="r", encoding="utf-8") as file:
        lines = file.readlines()
        isReadingIngredients = False
        for line in lines:
            if line == '\n':
                isReadingIngredients = True
            else:
                if isReadingIngredients:
                    ingredients.append(int(line.strip()))
                else:
                    range_parts = line.strip().split('-')
                    ranges.append((int(range_parts[0]), int(range_parts[1])))

    return ingredients, ranges

def solve_part1(ingredients, ranges):
    fresh_ingredients = 0

    for ingredient in ingredients:
        if _is_fresh(ingredient, ranges):
            fresh_ingredients += 1

    return fresh_ingredients

def _is_fresh(ingredient, ranges):
    for range in ranges:
        if ingredient >= range[0] and ingredient <= range[1]:
            return True
    return False

def solve_part2(ranges):
    number_of_fresh_ids = 0
    sorted_ranges = sorted(ranges, key=lambda x: x[0])

    # Merge ranges
    merged_ranges = [sorted_ranges[0]]
    for current_range in sorted_ranges[1:]:
        last_merged = merged_ranges[-1]

        if current_range[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current_range[1])
        else:
            merged_ranges.append(list(current_range))
            
    # Count
    
    for _range in merged_ranges:
        number_of_fresh_ids += (_range[1] - _range[0] + 1)
    
    return number_of_fresh_ids

if __name__ == "__main__":
    main()