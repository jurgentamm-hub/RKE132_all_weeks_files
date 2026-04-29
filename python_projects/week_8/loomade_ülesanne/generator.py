import random

from reader import read_from_file

def generate_sentence(adjectives_path, animals_path, verbs_path):
    adjectives = read_from_file(adjectives_path)
    animals = read_from_file(animals_path)
    verbs = read_from_file(verbs_path)

    adjective = random.choice(adjectives)
    animal = random.choice(animals)
    verb = random.choice(verbs)

    sentence = f"The {adjective} {animal} {verb}"
    return sentence