#TSP , Stimulated Annealing Algorithm
def calculate_total_distance(path, distances):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distances[path[i]][path[i+1]]
    total_distance += distances[path[-1]][path[0]]  # Return to starting city
    return total_distance

def tsp_brute_force(distances):
    num_cities = len(distances)
    min_distance = float('inf')
    best_path = []

    def generate_permutations(n):
        if n == num_cities:
            total_distance = calculate_total_distance(path, distances)
            nonlocal min_distance, best_path
            if total_distance < min_distance:
                min_distance = total_distance
                best_path = path[:]
            return
        for i in range(num_cities):
            if i not in path:
                path.append(i)
                generate_permutations(n + 1)
                path.pop()

    path = []
    generate_permutations(0)
    return best_path, min_distance

# Example usage
if __name__ == "__main__":
    distances = [
        [0, 29, 20, 21],
        [29, 0, 15, 27],
        [20, 15, 0, 26],
        [21, 27, 26, 0]
    ]

    best_path, min_distance = tsp_brute_force(distances)
    print(f"Best path: {best_path}")
    print(f"Minimum distance: {min_distance}")