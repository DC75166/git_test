"""Combines multiple if else logic to derive rain sound combinations for different number combinations of 3,5,7, (3,5),(3,7),(5,7),(5,3),(7,5),(7,3),(3,5,7) and no combination"""
def convert(number):
    """If else logic for number combination"""
    result = ""
    if number%3==0:
        result+="Pling"
    if number%5==0:
        result+="Plang"
    if number%7==0:
        result+="Plong"
    return result or str(number)
