"""Reversing a text."""
def reverse(text):
    """Reversing a string. Iterating the string and appending each character before the last character"""
    new_word = ""
    for char in text:
        new_word=char+new_word
    return new_word
        