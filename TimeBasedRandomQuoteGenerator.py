#Time-based Random Quote Generator:
import random
import datetime

def generate_random_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Innovation distinguishes between a leader and a follower. - Steve Jobs",
        "Stay hungry, stay foolish. - Steve Jobs"
        # Add more quotes here
    ]
    current_hour = datetime.datetime.now().hour
    random.seed(current_hour)  # Generate the same random quote within the same hour
    random_quote = random.choice(quotes)
    return random_quote

quote = generate_random_quote()
print(quote)