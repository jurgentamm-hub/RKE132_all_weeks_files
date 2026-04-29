from generator import generate_sentence


adjectives_path = read_from_file(r"week_8\loomade_ülesanne\adjectives.txt")
animals_path = read_from_file(r"week_8\loomade_ülesanne\animals.txt")
verbs_path = read_from_file(r"week_8\loomade_ülesanne\verbs.txt")


sentence = generate_sentence(adjectives_path, animals_path, verbs_path)
print(sentence)