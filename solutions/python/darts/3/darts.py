"""This code calculates the distance of a random coordinate inside concentric circles from the center and accordingly returns scores. Closer to the center means more score."""
def score(x_coordinate, y_coordinate):
    """Solution to exercism dart problem"""
    distance = ((x_coordinate**2)+ (y_coordinate**2))**0.5
    if 5<distance<=10:
        return 1
    if 1<distance<=5:
        return 5
    if 0<=distance<=1:
        return 10
    return 0
         