import string


def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    onlyLetters = filter(lambda x: x.isalpha(), list(sentence))
    characterSet = set(map(lambda x: x.lower(), onlyLetters))
    return characterSet == alphabet
