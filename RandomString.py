import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

# Example usage:
string_length = 8
random_string = generate_random_string(string_length)
print(random_string)
