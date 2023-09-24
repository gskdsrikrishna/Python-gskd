import random

def randomly_select_items(items, num_items):
    random_items = random.sample(items, num_items)
    return random_items

# Example usage:
my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig']
num_selections = 3
random_selections = randomly_select_items(my_list, num_selections)
print(random_selections)
