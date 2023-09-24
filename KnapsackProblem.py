#Knapsack Problem
def knapsack(items, capacity):
    if not items or capacity == 0:
        return 0
    
    weight, value = items[0]
    if weight > capacity:
        return knapsack(items[1:], capacity)
    
    include = value + knapsack(items[1:], capacity - weight)
    exclude = knapsack(items[1:], capacity)
    
    return max(include, exclude)

# Example usage
if __name__ == "__main__":
    items = [(2, 12), (1, 10), (3, 20), (2, 15)]
    capacity = 5
    
    max_value = knapsack(items, capacity)
    print(f"Maximum value that can be obtained: {max_value}")