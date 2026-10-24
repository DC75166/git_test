def is_armstrong_number(number):
    """Extract the last digit in each iteration, raise it to the power of the number's length, and add it to the total. Store the original number separately and use floor division (//) to remove the last digit in each iteration."""
    pass
    temp = 0
    orig = number
    count = len(str(number))
    while orig!=0:
        last = orig%10
        temp+=pow(last,count)
        orig//=10
    return temp == number 
        
