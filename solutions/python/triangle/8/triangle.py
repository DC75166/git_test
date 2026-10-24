"""Functions to determine whether a triangle is equilateral, isosceles, or scalene."""


def equilateral(sides):
    """Check if the triangle is equilateral."""
    return sides[0] == sides[1] == sides[2] > 0


def isosceles(sides):
    """Check if the triangle is isosceles."""
    side1, side2, side3 = sorted(sides)

    if side1 <= 0 or side1 + side2 <= side3:
        return False

    return side2 in {side1, side3}


def scalene(sides):
    """Check if the triangle is scalene."""
    side1, side2, side3 = sorted(sides)

    if side1 <= 0 or side1 + side2 <= side3:
        return False

    return len(set(sides)) == 3