def square(number):
    """This is a G.P series. So calculating the number of grains by the G.p term finding formula a(n) = a.(common.ratio)^n-1"""
    pass
    grain = 0
    while 1<=number<=64:
        grain = pow(2,number-1)
        return grain
    raise ValueError("square must be between 1 and 64")

def total():
    """This is a G.P series. So calculating the total number of grains by the G.p sum finding formula s(n) = a.((common.ratio)^n)-1)/common.ratio-1"""
    pass
    total = (pow(2,64)-1)
    return total
