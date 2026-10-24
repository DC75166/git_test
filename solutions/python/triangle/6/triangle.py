"""Checks if the traingle is equilateral or not"""
def equilateral(sides):
    pass
    return sides[0] == sides[1] == sides[2] > 0

"""Checks if the traingle is isosceles or not"""
def isosceles(sides):
    pass
    side1, side2, side3 = sorted(sides)
    
    # 1. Reject 0, negatives, and triangle inequality violations
    if side1<0 or (side1+side2<side3):
        return False
        
    # 2. Your logic checking if at least two sides match
    return side2 in {side1,side3}

"""Checks if the traingle is scalene or not"""
def scalene(sides):
    pass
    side1, side2, side3 = sorted(sides)
    
    # 1. Reject 0, negatives, and triangle inequality violations
    if side1<0 or (side1+side2<side3):
        return False
        
    # 2. Your logic checking that all three sides are unique
    return len(set(sides)) == 3
