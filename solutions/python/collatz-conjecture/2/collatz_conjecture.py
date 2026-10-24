"""This is a collatz conjencture. It states that whatever number we start with if rule is followed we will end up at 1. If even divdie by 2, if odd multiply 3 and add 1. Ultimately we will end up at 1. Here we count the steps needed to reach 1 and throw an error if the number is 0 or negative"""
def steps(number):
    """Collatz conjecture steps finding problem"""
    pass
    count = 0
    if number<=0:
        raise ValueError("Only positive integers are allowed")
    while number>1:
        if number%2==0:
            number//=2
            count+=1
        else:
            number= (number*3)+1
            count+=1
    return count
