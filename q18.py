# Implement a recursive function to calculate the sum of digits of a given number.

def cal(no):
    return no % 10 + cal(no // 10)

print(cal(54321))
