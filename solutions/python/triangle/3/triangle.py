def equilateral(sides):
    pass
    return sides[0] == sides[1] == sides[2] > 0

def isosceles(sides):
    pass
    a, b, c = sorted(sides)
    
    # Check validity (if the two shortest sides can't beat the longest, it's invalid)
    if a <= 0 or (a + b <= c):
        return False
        
    # Optimized check: only two pairs can possibly match now
    return a == b or b == c

def scalene(sides):
    pass
    a, b, c = sorted(sides)
    
    # Check validity
    if a <= 0 or (a + b <= c):
        return False
        
    # Optimized check: if it's sorted, just ensure adjacent sides aren't equal
    return a != b and b != c
