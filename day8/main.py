import math

def get_input(input_file):
    positions = []
    with open(input_file, 'r', encoding="utf-8") as file:
        positions = [[int(num) for num in line.strip().split(',')] for line in file.readlines()]

    return positions

class UnionFind:
    def __init__(self, size):
      
        # Initialize the parent array with each 
        # element as its own representative
        self.parent = list(range(size))

    def find(self, i):
        # If i itself is root or representative
        if self.parent[i] == i:
            return i
        # Else recursively find the representative 
        # of the parent
        return self.find(self.parent[i])

    def unite(self, i, j):
        # Representative of set containing i
        irep = self.find(i)
        # Representative of set containing j
        jrep = self.find(j)
        # Make the representative of i's set
        # be the representative of j's set
        self.parent[irep] = jrep

def solve_part1(positions):
    uf = _get_pairs_in_order(positions, 1000)

    # Count circuit sizes
    circuit_sizes = {}
    for i in range(len(positions)):
        root = uf.find(i)
        circuit_sizes[root] = circuit_sizes.get(root, 0) + 1

    # Get all circuit sizes and sort them
    sizes = sorted(circuit_sizes.values(), reverse=True)

    # Multiply the three largest
    if len(sizes) >= 3:
        result = sizes[0] * sizes[1] * sizes[2]
        print(result)
        return result

    return None

def _get_pairs_in_order(positions, pairs_to_make):
    n = len(positions)
    uf = UnionFind(n)
    connections_made = 0

    # Calculate all pairwise distances
    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = _get_distance(positions[i], positions[j])
            distances.append((dist, i, j))

    # Sort by distance
    distances.sort()

    # Try to make connections from the shortest pairs
    for attempt in range(min(pairs_to_make, len(distances))):
        dist, i, j = distances[attempt]

        # Try to connect - only count if they weren't already connected
        if uf.unite(i, j):
            connections_made += 1

    return uf

def _get_distance(pos1, pos2):
    return math.dist(pos1, pos2)

def main():
    data = get_input("input.txt")
    solve_part1(data)

if __name__ == "__main__":
    main()