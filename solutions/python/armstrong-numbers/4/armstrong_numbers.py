"""Armstrong problem"""
def is_armstrong_number(number):
    """This is an armstrong problem. We are extracting the last digit at each iteration and adding that in temp after raising it to the power of the original number's length. We divide the original number each time by 10 untill it reaches 0 to extract the first part of the original number. Then we compare the original and the temp number to chec if both are same"""
    temp = 0
    orig = number
    count = len(str(number))
    while orig!=0:
        last = orig%10
        temp+=pow(last,count)
        orig//=10
    return temp == number 
        
