import string


def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    only_letters = filter(lambda x: x.isalpha(), list(sentence))
    character_set = set(map(lambda x: x.lower(), only_letters))
    return character_set == alphabet
