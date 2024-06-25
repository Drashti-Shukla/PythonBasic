# Create a class representing a basic calculator with methods for addition, subtraction, multiplication, and division.

class Cal:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Cannot divide by zero."


cal = Cal()
print(cal.add(2,2))

