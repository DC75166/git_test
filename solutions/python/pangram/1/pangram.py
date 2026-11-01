import string
def is_pangram(sentence):
    pass
    lowercase = string.ascii_lowercase
    sentence_set = {char for char in sentence.lower() if char.isalpha()}

    return set(lowercase).issubset(sentence_set)