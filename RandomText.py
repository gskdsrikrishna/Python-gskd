import random
import string

def generate_random_text(length):
    text = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation + ' ', k=length))
    return text

# Example usage:
text_length = 100
random_text = generate_random_text(text_length)
print(random_text)
