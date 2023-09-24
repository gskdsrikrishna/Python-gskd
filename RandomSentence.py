import random

def generate_random_sentence():
    nouns = ['cat', 'dog', 'house', 'car', 'tree']
    verbs = ['runs', 'jumps', 'sleeps', 'eats', 'drives']
    adjectives = ['big', 'small', 'red', 'green', 'happy']
    adverbs = ['quickly', 'slowly', 'loudly', 'quietly', 'happily']
    
    random_noun = random.choice(nouns)
    random_verb = random.choice(verbs)
    random_adjective = random.choice(adjectives)
    random_adverb = random.choice(adverbs)
    
    sentence = f"The {random_adjective} {random_noun} {random_verb} {random_adverb}."
    return sentence

# Example usage:
random_sentence = generate_random_sentence()
print(random_sentence)
