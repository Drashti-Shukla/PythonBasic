# Implement a function to check if a given year is a leap year.
from datetime import date, datetime


def check_leap(year):
    if year % 4 == 0:
        return "Leap Year"
    else:
        return "Not Leap Year"


year = (int(input("Enter a date:")))
print(check_leap(year))
