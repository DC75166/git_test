def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    sum = 0
    i = 1
    if number<1:
        raise ValueError("Classification is only possible for positive integers.")
    while i*i<=number:
        if number%i==0:
            pair = number//i
            if i!=number:
                sum+=i
            if pair not in (number, i):
                sum+=pair
        i+=1
    if sum<number:
        return "deficient"
    if sum>number:
        return "abundant"
    return "perfect"

