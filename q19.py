# Write a program to calculate the area of a rectangle, allowing the user to input the length and width.

def area(l,w):
    return l*w

l=int(input("Enter Length of Rectangle:"))
w=int(input("Enter Width of Rectangle:"))
print("Area of Rectangle:",area(l,w))