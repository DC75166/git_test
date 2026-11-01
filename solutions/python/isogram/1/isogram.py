"""Finding an isogram problem"""
def is_isogram(phrase):
    """Solution for finding an isogram. Created a letters set that only has the alphabets. Created phrase_length variable that increments 1 every time it finds an alphabet in the string. Then we compare the length of the set with the phrase_length variable"""
    # new_set = set(phrase)
    # return len(new_set)==len(phrase)
    # new_phrase=""
    # for char in phrase.lower():
    #     if char.isalpha():
    #         new_phrase+=char
    # new_set = set(new_phrase)
    # return len(new_set)==len(new_phrase)

    normalised_phrase = phrase.lower()
    letters = {char for char in normalised_phrase if char.isalpha()}
    phrase_length = sum(1 for char in normalised_phrase if char.isalpha())
    return len(letters)==phrase_length

    # return len({char for char in normalised_phrase if char.isalpha()}) == sum(1 for char in normalised_phrase if char.isalpha())