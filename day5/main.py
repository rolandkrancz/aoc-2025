
def main():
    ingredients, ranges = get_input()
    result = solve_part1(ingredients, ranges)
    print(f"Part 1 result: {result}")

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

if __name__ == "__main__":
    main()