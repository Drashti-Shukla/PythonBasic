# Implement a function to find the greatest common divisor (GCD) of two numbers.
import math


def gcd(a,b):
    print(math.gcd(a,b))
    # if (b == 0):
    #     return a
    # else:
    #     return gcd(b, a % b)


no1=int(input("Enter Number:"))
no2=int(input("Enter Number:"))
gcd(no1,no2)