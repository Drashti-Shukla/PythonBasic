# Create a Python script that checks if a given string is a palindrome.

# def palidrome(no):
#     temp = no
#     s = 0
#     while (no > 0):
#         l = no % 10
#         s = s * 10 + l
#         no = no // 10
#         print(l, no, s)
#     if (s == temp):
#         return "Palindrome"
#     else:
#         return "Not Palindrome"
#
#
# no = int(input("Enter Number:"))
# print(f"{no} is {palidrome(no)}")
#

def str_palindrome():
    word = input("Enter a word: ")
    is_palindrome = word == word[::-1]
    print("Palindrome" if is_palindrome else "Not Palindrome")

str_palindrome()