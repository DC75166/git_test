"""Checks if a given year is leap year or not"""
def leap_year(year):
    pass
    return year%400==0 or (
        year%4==0 and year%100!=0
    )
    
