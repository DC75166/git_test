"""Solution to finding perfect number accd to Nicomachus's law"""
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    divisor_sum = 0
    iterator = 1
    if number<1:
        raise ValueError("Classification is only possible for positive integers.")
    while iterator*iterator<=number:
        if number%iterator==0:
            pair = number//iterator
            if iterator!=number:
                divisor_sum+=iterator
            if pair not in (number, iterator):
                divisor_sum+=pair
        iterator+=1
    if divisor_sum<number:
        return "deficient"
    if divisor_sum>number:
        return "abundant"
    return "perfect"