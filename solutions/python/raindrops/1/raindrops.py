"""Combines multiple if else logic to derive rain sound combinations for different number combinations of 3,5,7, (3,5),(3,7),(5,7),(5,3),(7,5),(7,3),(3,5,7) and no combination"""
def convert(number):
    """If else logic for number combination"""
    result = ""
    if number%3==0:
        if number%5==0:
            if number%7==0:
                return result+"PlingPlangPlong"
            return result+"PlingPlang"
        if number%7==0:
            return result+"PlingPlong"
        return result+"Pling"
    if number%5==0:
        if number%7==0:
            return result+"PlangPlong"
        return result+"Plang"
    if number%7==0:
        return result+"Plong"
    return str(number)
