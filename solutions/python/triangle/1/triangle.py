def equilateral(sides):
    pass
    return sides[0] == sides[1] == sides[2] > 0

def isosceles(sides):
    pass
    a, b, c = sides
    
    # 1. Reject 0, negatives, and triangle inequality violations
    if a <= 0 or b <= 0 or c <= 0 or (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
        
    # 2. Your logic checking if at least two sides match
    return a == b or b == c or a == c

def scalene(sides):
    pass
    a, b, c = sides
    
    # 1. Reject 0, negatives, and triangle inequality violations
    if a <= 0 or b <= 0 or c <= 0 or (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
        
    # 2. Your logic checking that all three sides are unique
    return len(set(sides)) == 3
