import random

def generate_random_name():
    first_names = ['John', 'Emma', 'Michael', 'Sophia', 'William', 'Olivia']
    last_names = ['Smith', 'Johnson', 'Brown', 'Taylor', 'Miller', 'Davis']
    
    random_first_name = random.choice(first_names)
    random_last_name = random.choice(last_names)
    
    return random_first_name + ' ' + random_last_name

# Example usage:
random_name = generate_random_name()
print(random_name)
