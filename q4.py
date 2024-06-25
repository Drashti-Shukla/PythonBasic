# Write a program to find the factorial of a number using a recursive function.

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


no = int(input("Enter Number:"))
print(f"Factorial of {no} is {factorial(no)}")